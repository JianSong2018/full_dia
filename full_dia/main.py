#!/usr/bin/env python
from full_dia import utils
from full_dia import cross
from full_dia.log import Logger
from full_dia.library import Library

from full_dia.main_core import *

try:
    # profile
    profile = lambda x: x
except:
    profile = lambda x: x

logger = Logger.get_logger()

@profile
def main():
    # init ws, lib, out_name
    ws_global, dir_lib, out_name = utils.get_args()
    utils.init_multi_ws(ws_global, out_name)

    # lib
    lib = Library(dir_lib)

    # search
    cfg.phase = 'First'
    main_search(lib)

    # global
    logger.info(f'=================Global Analysis=================')
    df_global1 = cross.cal_global(
        lib, cfg.top_k_fg, cfg.top_k_pr, multi_ws=cfg.multi_ws
    )
    # utils.print_external_global_fdr(df_global1)
    cross.save_report_result(df_global1, multi_ws=cfg.multi_ws)
    logger.info('Finished.')
    return

    # if reanalysis
    utils.save_lib(df_global1)

    # modify lib
    lib.polish_lib_by_idx(df_global1['pr_index'])

    # search
    cfg.phase = 'Second'
    df_v = main_search(lib)

    # second global
    logger.info(f'=================Second Global Analysis=================')
    df_global = cross.cal_global(
        lib, cfg.top_k_fg, cfg.top_k_pr, df_v=df_v, df_global1=df_global1
    )
    utils.print_external_global_fdr(df_global)
    cross.save_report_result(df_global, df_v=df_v)

    logger.info('Finished.')


if __name__ == '__main__':
    main()