from datetime import datetime

class Incident:
    """Представляет собой объект инцидента в системе IRP.

    Attributes:
        name (str): Название инцидента, генерируемое по шаблону. 
            Пример: 'Подозрение на брутфорс с успешной авторизацией на related_addresses'.
            Название поля в MP SIEM: incident.name
        description (str): Любое описание инцидента,которое может как заполнятся автоматически,давая советы и успешные практики для аналитика,так и дополнятся вручную.
            Пример: 'Рекомендуется блокировка учетной записи и смена пароля'.
            Название поля в MP SIEM: incident.description
        status (str): Текущий статус инцидента ['Создан','Взят в работу','Закрыт']. 
            Допустимые значения: 'Создан', 'Взят в работу', 'Закрыт'.
            Название поля в MP SIEM: object.state
        source (str): Источник алерта AV,IDS,SIEM,сообщение от пользователя.
            Название поля в MP SIEM: event_src.category
        timestamp (datetime): Временная метка в формате DateTime YYYY-MM-DD'T'HH:MM:SS.
            Название поля в MP SIEM: subevents.time
        category (str): Категория инцидента ['BruteForce','DataLeak','Ransomware',....].
            Название поля в MP SIEM: incident.category
        severity (str): Критичность инцидента ['low','medium','high','critical']. 
            Название поля в MP SIEM: incident.severity
        assigned_uid (str): Сотрудник/Отдел назначенный ответсвенным за реагирование иницидент.
            Название поля в MP SIEM: incident.assigned_to_user_id
        related_addresses (List[str]): IP адресс машин на которые направлена атака.
            Название поля в MP SIEM: incident.related_addresses
        fqdn (str): Полное доменное имя затронутого узла (например, 'workstation01.corp.local').
            Название поля в MP SIEM: event_src.fqdn
        affected_user (str): Имя скомпрометированной учетной записи.
            Название поля в MP SIEM: object.account.name
        user_role (str): Роль пользователя.
            Название поля в MP SIEM: object.account.privileges
        domain (str): Имя домена, в котором зафиксирован инцидент (например, 'corp.local').
            Название поля в MP SIEM: object.domain
        ext_address (str): Внешние IP адресса атакующих.
            Название поля в MP SIEM: incident.attacking_addresses
        iocs (str): Индекс компроментации.Хэши,домены,url endpoints,IPs,тактики,техники.
            Название поля в MP SIEM: alert.ioc_value
        is_false_positive (bool): Флаг ложноположительного срабатывания.
        details (Dict[str, Any]): Поле для обогащенных данных из внешних систем.
            Сюда записываются результаты из VirusTotal, Shodan, AD info и тп.
            Название поля в MP SIEM: body
    """

    def __init__(self, 
                 name: str, 
                 description: str, 
                 status: str, 
                 source: str, 
                 timestamp: datetime, 
                 category: str, 
                 severity: str, 
                 assigned_uid: str, 
                 related_addresses: list[str], 
                 fqdn: str,
                 domain: str,
                 affected_user: str,
                 user_role: str,
                 ext_address: str, 
                 iocs: str,
                 is_false_positive: bool,
                 details: dict[str, any]):
        self.name = name
        self.description = description
        self.status = status
        self.source = source
        self.timestamp = timestamp
        self.category = category
        self.severity = severity
        self.assigned_uid = assigned_uid
        self.related_addresses = related_addresses
        self.fqnd = fqdn
        self.domain = domain
        self.affected_user = affected_user
        self.user_role = user_role
        self.ext_address = ext_address
        self.iocs = iocs
        self.is_false_positive = is_false_positive
        self.details = details
