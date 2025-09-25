import json
import queue

from common.basePage import BasePage




def qte(bp: BasePage, params_str):
    params = json.loads(params_str)
    qte_input_mask = params[0]
    qte_input = params[1]
    bp.qte_queue = queue.Queue()

    cur = 0
    while cur < 6:
        # if qte_input_mask & (1 << cur) == 0:
        #     cur += 1
        #     continue
        is_on = qte_input & (1 << cur) != 0
        # is_change = qte_input_mask & (1 << cur) != 0
        if is_on:
            bp.qte_queue.put(cur)
            cur += 1
            continue
        cur += 1
