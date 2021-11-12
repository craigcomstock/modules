import io
import sys

from configparser import ConfigParser
from cfengine import PromiseModule, ValidationError, Result

class IniPromiseTypeModule(PromiseModule):
  def validate_promise(self, promiser, attributes):
    if not promiser.startswith("/"):
      raise ValidationError("File path '%s' must be absolute" % promiser)
  def evaluate_promise(self, promiser, attributes):
    if not promiser.startswith("/"):
      raise ValidationError("File path '%s' must be absolute" % promiser)
    self.log_info("promiser is '%s'" % promiser)
    config = ConfigParser(strict=False)
# TODO, determine if the file HAD a section or not, and write out accordingly later
#    with open(promiser) as stream:
#      config.read_string("[top]\n" + stream.read())
    with open(promiser, 'a') as stream:
      self.log_info("got the stream")
      text=stream.read()
      self.log_info("stream was '%s'" % text)
      config.read_string(text)
      output = io.StringIO()
      config.write(output)
      self.log_info("config is %s" % output.getvalue())
      self.log_info("config is of type %s" % type(config))
#      config.write(stream)

    return Result.KEPT;


if __name__ == "__main__":
  IniPromiseTypeModule().start()
