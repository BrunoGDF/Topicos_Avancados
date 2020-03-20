class usuario(base):
    tablename = 'usuario'

        usuarioId = Column(Integer, primary_key=True)
        descricao  = Column(String)
