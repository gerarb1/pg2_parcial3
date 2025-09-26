from .validators import ValidadorDatosPersonales, ValidadorDatosContacto

class PersonaBuilder:
    def __init__(self):
        self._persona = Persona()
    """Builder para crear instancias de Persona de forma segura y modular.

    Permite establecer datos personales y de contacto paso a paso con validación
    automática antes de construir el objeto Persona final.

    Métodos:
        set_datos_personales(nombre, edad, documento) -> PersonaBuilder
            Establece los datos personales con validación.
            Args:
                nombre (str): Nombre de la persona (solo letras).
                edad (str): Edad de la persona (número positivo < 150).
                documento (str): Documento de identidad (alfanumérico, >= 6 caracteres).
            Raises:
                ValueError: Si los datos no pasan la validación.

        set_datos_contacto(email, celular, direccion) -> PersonaBuilder
            Establece los datos de contacto con validación.
            Args:
                email (str): Dirección de email válida (contiene @ y .).
                celular (str): Número de celular (9-10 dígitos).
                direccion (str): Dirección con al menos una letra.
            Raises:
                ValueError: Si los datos no pasan la validación.

        build() -> Persona
            Construye y retorna la instancia de Persona con los datos validados.
            Returns:
                Persona: Instancia completa de la clase Persona.
    """
    def set_datos_personales(self, nombre, edad, documento):
        validador = ValidadorDatosPersonales()
        if validador.validar_nombre(nombre) and validador.validar_edad(edad) and validador.validar_documento_identidad(documento):
            self._persona._nombre = nombre
            self._persona._edad = edad
            self._persona._documento = documento
        else:
            raise ValueError("Datos personales inválidos")
        return self

    def set_datos_contacto(self, email, celular, direccion):
        validador = ValidadorDatosContacto()
        if validador.validar_email(email) and validador.validar_celular(celular) and validador.validar_direccion(direccion):
            self._persona._email = email
            self._persona._celular = celular
            self._persona._direccion = direccion
        else:
            raise ValueError("Datos de contacto inválidos")
        return self

    def build(self):
        return self._persona

class Persona:
    """Representa una persona con datos personales y de contacto.

    Atributos:
        _nombre (str): Nombre de la persona.
        _edad (str): Edad de la persona.
        _documento (str): Documento de identidad.
        _email (str): Dirección de email.
        _celular (str): Número de celular.
        _direccion (str): Dirección de la persona.

    Métodos:
        __str__() -> str
            Devuelve una representación en cadena de la persona.
    """
    def __init__(self):
        self._nombre = None
        self._edad = None
        self._documento = None
        self._email = None
        self._celular = None
        self._direccion = None

    def __str__(self):
        return (f"Persona: {self._nombre}, Edad: {self._edad}, Documento: {self._documento}, "
                f"Email: {self._email}, Celular: {self._celular}, Dirección: {self._direccion}")