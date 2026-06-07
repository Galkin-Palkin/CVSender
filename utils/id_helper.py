from aiogram.fsm.context import FSMContext

class IdHelper:
    @staticmethod
    def extract_id(callback_data: str) -> str:
        return callback_data.split(':')[-1]
    
    @staticmethod
    async def add_id_to_state(callback_data: str, state: FSMContext, id_key: str) -> str:
        id_value = IdHelper.extract_id(callback_data)
        data = await state.get_data()
        await state.set_data({**data, id_key: id_value})
        return id_value
    
    @staticmethod
    async def get_id_from_state(state: FSMContext, id_key: str) -> str:
        data = await state.get_data()
        return data.get(id_key)
    