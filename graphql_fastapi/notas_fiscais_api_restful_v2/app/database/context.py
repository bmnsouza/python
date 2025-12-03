from app.database.session import get_session


async def get_context():
    """
    Contexto assíncrono usado pelo Strawberry GraphQL.
    Cria uma sessão de banco por requisição e injeta no campo `info.context["session"]`.
    """
    async for session in get_session():
        try:
            yield {"session": session}
        finally:
            await session.close()
