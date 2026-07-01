# -*- coding: utf-8 -*-
"""
音频播放器模块
支持语音合成和音频播放
"""

import os
import threading
from urllib.parse import quote


class AudioPlayer:
    """音频播放管理类"""

    def __init__(self):
        """初始化音频播放器"""
        self.audio_dir = os.path.join(os.path.dirname(__file__), "resources", "audio")

        # 确保音频目录存在
        if not os.path.exists(self.audio_dir):
            os.makedirs(self.audio_dir)

        # 可用发音人
        self.voices = {
            "zh-CN": "中文女声",
            "hani": "哈尼语母语者",
        }

        self.current_player = None

    def speak(self, text, lang="zh-CN"):
        """
        语音合成播放

        Args:
            text: 要朗读的文本
            lang: 语言代码 ('zh-CN' 或 'hani')
        """
        if not text:
            return

        # 根据语言选择播放方式
        if lang == "zh-CN":
            self._speak_chinese(text)
        else:
            self._speak_hani(text)

    def _speak_chinese(self, text):
        """
        播放中文普通话

        使用系统TTS或第三方TTS服务
        """
        # 检查是否有本地音频文件
        # 优先使用预录制的中文音频
        # 否则使用系统TTS或网络TTS

        try:
            # 方法1: 尝试使用pyttsx3 (离线TTS)
            import pyttsx3

            engine = pyttsx3.init()
            engine.setProperty("rate", 150)  # 语速
            engine.setProperty("volume", 1.0)  # 音量
            engine.say(text)
            engine.runAndWait()
        except ImportError:
            # 方法2: 使用系统自带TTS (Windows)
            try:
                import win32com.client

                speaker = win32com.client.Dispatch("SAPI.SpVoice")
                speaker.Speak(text)
            except:
                # 方法3: 使用网络TTS (有网络时)
                self._speak_online(text, "zh-CN")
        except Exception as e:
            print(f"语音播放失败: {e}")

    def _speak_hani(self, text):
        """
        播放哈尼语

        优先使用本地母语者录制的音频
        """
        # 先查找是否有对应的本地音频文件
        # 本地词库中有audio_hani字段的可以使用

        # 由于没有本地录音，使用网络TTS
        self._speak_online(text, "hani")

    def _speak_online(self, text, lang):
        """
        在线语音合成（需要网络）

        Args:
            text: 文本
            lang: 语言
        """
        # 可以使用免费的在线TTS服务
        # 这里使用Google Translate TTS作为示例
        try:
            from urllib.request import urlopen, Request
            import urllib.parse

            if lang == "zh-CN":
                tts_lang = "zh-CN"
            else:
                # 哈尼语使用相近语言代替或使用变通方法
                tts_lang = "vi"  # 越南语与哈尼语有些相近

            url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(text)}&tl={tts_lang}&total=1&idx=0&textlen={len(text)}&client=tw-ob"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }

            req = Request(url, headers=headers)
            response = urlopen(req, timeout=5)

            # 播放音频
            import playsound
            from io import BytesIO

            audio_data = response.read()

            # 保存到临时文件
            import tempfile

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                f.write(audio_data)
                temp_file = f.name

            # 播放
            playsound.playsound(temp_file)

            # 删除临时文件
            os.unlink(temp_file)

        except Exception as e:
            print(f"在线语音播放失败: {e}")
            # 静默失败，不影响用户体验

    def play(self, audio_file):
        """
        播放本地音频文件

        Args:
            audio_file: 音频文件路径
        """
        if not os.path.exists(audio_file):
            print(f"音频文件不存在: {audio_file}")
            return

        try:
            import playsound

            playsound.playsound(audio_file)
        except ImportError:
            print("请安装 playsound 库: pip install playsound")
        except Exception as e:
            print(f"音频播放失败: {e}")

    def get_voice_list(self):
        """
        获取可用发音人列表

        Returns:
            dict: 发音人信息
        """
        return self.voices

    def get_audio_path(self, audio_name):
        """
        获取音频文件路径

        Args:
            audio_name: 音频文件名

        Returns:
            str: 完整路径
        """
        return os.path.join(self.audio_dir, audio_name)


class VoiceRecorder:
    """语音录制类"""

    def __init__(self):
        """初始化录音器"""
        self.recording = False
        self.audio_data = None

    def start_recording(self):
        """开始录音"""
        try:
            import pyaudio
            import wave

            self.recording = True
            self.audio_data = []

            # 录音参数
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 16000

            p = pyaudio.PyAudio()

            stream = p.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
            )

            frames = []

            while self.recording:
                data = stream.read(CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            return frames

        except ImportError:
            print("请安装 pyaudio 库: pip install pyaudio")
            return None

    def stop_recording(self):
        """停止录音"""
        self.recording = False

    def recognize_speech(self, audio_data):
        """
        语音识别

        Args:
            audio_data: 音频数据

        Returns:
            str: 识别结果文本
        """
        # 可以使用在线语音识别服务
        # 如 讯飞语音识别、百度语音识别等
        pass


class SpeechRecognizer:
    """语音识别类"""

    def __init__(self):
        """初始化语音识别"""
        self.language = "zh-CN"

    def recognize(self, audio_file=None, audio_data=None):
        """
        语音识别

        可以使用:
        - 讯飞语音识别API
        - 百度语音识别API
        - Google Speech-to-Text

        Args:
            audio_file: 音频文件路径
            audio_data: 音频数据

        Returns:
            str: 识别结果
        """
        # 示例使用Google Speech Recognition
        try:
            import speech_recognition as sr

            recognizer = sr.Recognizer()

            if audio_file:
                with sr.AudioFile(audio_file) as source:
                    audio = recognizer.record(source)
            elif audio_data:
                # 需要处理音频数据
                pass

            # 使用Google识别（需要网络）
            result = recognizer.recognize_google(audio, language=self.language)
            return result

        except ImportError:
            print("请安装 speech_recognition 库")
            return ""
        except Exception as e:
            print(f"语音识别失败: {e}")
            return ""
