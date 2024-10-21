import numpy as np
from typing import Any, Dict, List, Optional, Tuple
from docetl.operations.base import BaseOperation

from . import speaker

class SpeakerOperation(BaseOperation):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

    def syntax_check(self) -> None:
        pass

    def execute(
        self, input_data: List[Dict], is_build: bool = False
    ) -> Tuple[List[Dict], float]:
        """
        Executes the text to speech operation on the input data.

        Args:
            input_data (List[Dict]): A list of dictionaries to process.
            is_build (bool): Whether the operation is being executed
              in the build phase. Defaults to False.

        Returns:
            Tuple[List[Dict], float]: A tuple containing the input items
              with a path to a soundfile added.
        """
        if not input_data:
            return input_data, 0

        output = []
        for idx, (item, audio) in enumerate(zip(
                input_data,
                speaker.render_conversation(
                    input_data,
                    voices = self.config.get("voices", None),
                    speaker_key = self.config.get("speaker_key", "speaker"),
                    text_key = self.config.get("text_key", "text")
                ))):
            item = dict(item)
            path = os.path.join(
                self.config.get("output_dir", "."),
                "%s.%s" % (idx, self.config.get("output_format", "mp3")))
            audio.export(path)
            item[self.config.get("output_key", "sound")] = path
            output.append(item)
            
        return output, 0
