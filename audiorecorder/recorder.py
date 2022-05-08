from PySide6.QtWidgets import QWidget
from audiorecorder.view import Ui_main_widget


class AudiorecorderController(QWidget):
    def __int__(self):
        super().__init__()
        self.audio_recorder_view = Ui_main_widget()
        self.audio_recorder_view.setupUi(self)

        self.record_button = self.audio_recorder_view.start_button
        self.record_button.clicked.connected(self.record)
        self.record_progress = self.audio_recorder_view.progress_bar

        self.record_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        self.record_duration = 10
        self.record_file_name = "my-audio.mp3"
        self.record_size = 96

    def record(self):
        if self.record_url != '':
            pass

