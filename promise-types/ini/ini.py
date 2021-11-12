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
    config = ConfigParser(strict=False)
    with open(promiser) as stream:
      config.read_string("[top]\n" + stream.read())
    self.log_info("config is 
    return Result.KEPT;


if __name__ == "__main__":
  IniPromiseTypeModule().start()
