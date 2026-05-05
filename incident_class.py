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
        source (str): Источник алерта AV,IDS,SIEM,сообщение от пользователя.
            Название поля в MP SIEM: event_src.category
        timestamp (datetime): Временная метка в формате DateTime YYYY-MM-DD'T'HH:MM:SS.
            Название поля в MP SIEM: subevents.time
        close_timestamp (datetime): Временная метка закрытия инцидента в формате DateTime YYYY-MM-DD'T'HH:MM:SS.
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
            Название поля в MP SIEM: alert.context
    """

    def __init__(self,siem_alert: dict[str,any]):
        
        self.mapping_mp_siem(siem_alert)

    def get_details_as_json(input_json_string) -> dict:
        """
        Преобразует всю обогащенную инфу в формат


        "ИСТОЧНИК":"ИНФОРМАЦИЯ" 
        
        str:str
        
        """
        
        pass

    def mapping_mp_siem(self,siem_alert: dict[str,any]):
        self.name = siem_alert.get("incident.name","noname")
        self.description = siem_alert.get("incident.description","")
        self.status = "Создан"
        self.source = siem_alert.get("event_src.category","Источник не определен")
        self.timestamp = siem_alert.get("time",str(datetime.now()))
        self.closetimestamp = "-"
        self.category = siem_alert.get("incident.category","Тип не определен")
        self.severity = siem_alert.get("incident.severity","-")
        self.assigned_uid = siem_alert.get("incident.assigned_to_user_id","Отвественный не задан")
        self.related_addresses = siem_alert.get("incident.related_addresses",[])
        self.fqnd = siem_alert.get("incident.related_addresses",[])
        self.affected_user = siem_alert.get("object.account.name","-")
        self.user_role = siem_alert.get("object.account.privileges","-")
        self.domain = siem_alert.get("object.domain","-")
        self.ext_address = siem_alert.get("incident.attacking_addresses",[])
        self.iocs = siem_alert.get("alert.ioc_value","-")
        self.is_false_positive = False
        self.details = self.get_details_as_json(siem_alert.get("alert.context","{}"))