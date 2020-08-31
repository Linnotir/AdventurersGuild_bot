from aiogram import executor
from bin.main_var import dp, loop
import logging

from bot.functions.default.start_func import start_func, start_q1_func
from bot.states.default_states import start_states


# Logging
logging.basicConfig(format='--- %(asctime)s ---\n%(filename)s %(levelname)s in line %(lineno)s \n%(message)s',
level=logging.ERROR)#, filename='error.log', filemode='w')


# Handlers

'''<<<-----   DEFAULT   ----->>>'''
dp.register_message_handler(start_func, commands='start')
dp.register_message_handler(start_q1_func, state=start_states.Q1)

start_message= '''\
     　　 ／＞     フ 
　　　　　| 　_　 _| 
　 　　　／`ミ _x 彡 
　　 　 /　　　  | 
　　　 /　 ヽ　　ﾉ 
　／￣|　　 | | | 
　| (￣ヽ＿_ヽ_)_) 
　 ＼二つ

Bot already worked...
'''
print(start_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, loop=loop)