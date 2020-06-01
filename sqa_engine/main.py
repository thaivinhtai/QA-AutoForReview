#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Framework executor.
"""

from sys import path
from pathlib import Path


def main() -> None:
    """Main Function"""

    from sqa_engine.utilities.workspace_vars import\
        set_python_path_env_var, set_android_home_env_var,\
        inter_path, set_version_env_var, set_proxy
    from sqa_engine.utilities.args_handler import get_args
    from sqa_engine.utilities.executor import\
        execute_test_cases, copy_files, push_result
    from sqa_engine.utilities.framework_generator import\
        generate_sequence, generate_docs, generate_docs_folder

    set_python_path_env_var()
    set_proxy()
    args = get_args()

    set_version_env_var(args.version)

    if args.module.lower() == 'mobile_app'\
            and args.mobile_platform.lower() != 'ios':
        set_android_home_env_var()

    if args.gen_scripts:
        generate_docs_folder(module_name=args.module,
                             test_design=args.test_design,
                             version=args.version)
        generate_sequence(test_module=args.module,
                          test_design=args.test_design)
        generate_docs(test_module=args.module, test_design=args.test_design)
        return

    execute_test_cases(args)

    if args.run_job or args.push_result:
        push_result()
    return


if __name__ == "__main__":

    # Add workspace to python path, mark it as an Python lib
    path.append(str(Path(__file__).parent.absolute().parent.parent))
    # Add sqa_engine to python path
    path.append(str(Path(__file__).parent.absolute().parent))
    # run main engine
    main()
