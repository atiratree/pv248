from parse.arg_parser import ArgParser
from service.composers_service import ComposersService
from util.utils import Utils

if __name__ == "__main__":
    args = ArgParser.require_composer_args()
    composer_name = ArgParser.get_name_arg(args)
    Utils.print(ComposersService.get_composers_with_scores(composer_name), extra_newline=True)
