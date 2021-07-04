import cv2


class VideoIterator:
    def __init__(self, video) -> None:
        super().__init__()
        self.video = video
        self.read_complete: bool = False

    def get_next(self):
        if not self.read_complete:
            has_more, I = self.video.read()
            if not has_more:
                self.read_complete = True
                return None
            return I
        else:
            return None

    def has_more(self):
        return not self.read_complete


# CachingVideoIterator
class CachingVideoIterator(VideoIterator):

    def __init__(self, video) -> None:
        super().__init__(video)
        self.frames = []
        self.frame_index = 0

    def get_next(self):
        if not self.read_complete and self.frame_index == len(self.frames):
            has_more, I = self.video.read()
            if not has_more:
                self.read_complete = True
                return None
            else:
                self.frame_index += 1
                self.frames.append(I)
                return I

    def get_previous(self):
        if self.frame_index == 0:
            return None
        self.frame_index -= 1
        return self.frames[self.frame_index]


class VideoProcessor:
    def __init__(self, video_address: str) -> None:
        super().__init__()
        self.video_address = video_address
        self.video = cv2.VideoCapture(video_address)

    def get_video(self):
        return self.video

    def get_iterator(self) -> VideoIterator:
        return VideoIterator(self.video)

    def get_caching_iterator(self) -> CachingVideoIterator:
        return CachingVideoIterator(self.video)
