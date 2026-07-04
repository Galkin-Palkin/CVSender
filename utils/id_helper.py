from aiogram.fsm.context import FSMContext

class StateHelper:
    @staticmethod
    def extract_id(callback_data: str) -> str:
        return callback_data.split(':')[-1]
    
    @staticmethod
    async def add_id_to_state(callback_data: str, state: FSMContext, id_key: str) -> str:
        id_value = StateHelper.extract_id(callback_data)
        data = await state.get_data()
        await state.set_data({**data, id_key: id_value})
        return id_value
    
    @staticmethod
    async def get_value_from_state(state: FSMContext, key: str) -> str:
        data = await state.get_data()
        return data.get(key)
    
    @staticmethod
    async def add_value_to_state(state: FSMContext, key: str, value: str):
        data = await state.get_data()
        await state.set_data({**data, key: value})
