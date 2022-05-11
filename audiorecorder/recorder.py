import datetime
import sys
import urllib.request
from _thread import start_new_thread

from PySide6.QtWidgets import QWidget, QApplication
from audiorecorder.view import Ui_main_widget


class AudiorecorderController(QWidget):
    def __init__(self):
        super().__init__()

        # init and setup view:
        self.audio_recorder_view = Ui_main_widget()
        self.audio_recorder_view.setupUi(self)

        # init record button and connect click event
        self.record_button = self.audio_recorder_view.start_button
        self.record_button.clicked.connect(self.start_record)
        self.record_progress = self.audio_recorder_view.progress_bar

        # init default values
        self.record_url = "http://radios.rtbf.be/vivabxl-128.mp3"
        self.record_duration = 10
        self.record_file_name = "my-audio.mp3"
        self.record_size = 96

    def start_record(self):
        if self.audio_recorder_view.url_line_edit.text() != '':
            self.record_url = self.audio_recorder_view.url_line_edit.text()

        if self.audio_recorder_view.file_name_line_edit.text() != '':
            self.record_file_name = self.audio_recorder_view.file_name_line_edit.text()

        if int(self.audio_recorder_view.length_field.value()) > 0:
            self.record_duration = int(self.audio_recorder_view.length_field.value())
            self.audio_recorder_view.progress_bar.setMaximum(self.record_duration)
        if int(self.audio_recorder_view.size_spin_box.value()) > 0:
            self.record_size = int(self.audio_recorder_view.size_spin_box.value())

        # run record-function in own thread
        start_new_thread(self.record, ())

    def record(self):
        self.record_button.setText("Aufnahme läuft")
        start_time = datetime.datetime.now()
        audio_src = urllib.request.urlopen(self.record_url)
        with open(self.record_file_name, 'wb') as audio_dst:
            while (datetime.datetime.now() - start_time).seconds < self.record_duration:
                audio_dst.write(audio_src.read(self.record_size))
                self.audio_recorder_view.progress_bar.setValue((datetime.datetime.now() - start_time).seconds)
        self.record_button.setText("STARTEN")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    recorder = AudiorecorderController()
    recorder.show()
    sys.exit(app.exec())
