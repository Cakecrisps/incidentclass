class Assets:

    """
    Объект класса актив
    
    Источники данных для модуля инвентаризации:AD,KSC,SCCM,DHCP сервер,гипервизоры,ansible.
    
    Attributes:
        assets_name(string) - имя актива.
            Пример:WORKSTATION-1231,MPSIEMHOST-12222
            Мапинг в AD: CN
        domain_name(string) - доменное имя актива
            Пример: 123.sigma.corp
            Мапинг в AD: dNSHostName
        ip(string) - IP актив
            Пример: 192.168.1.2
        mac_address(string) - мак адресс устройства
            Пример: 02:50:C3:1C:FA:24
        organization(string) - организация к которой принадлежит хост
            Пример: организация
            Мапинг в AD: o / company
        responsible(string) - отвественный
            Мапинг в AD: managedBy
        os_name(string) - название операционной системы
            Пример: Windows 11 Pro 25H2
            Мапинг в AD: operatingSystem
        os_version(string) - версия ОС
            Пример: 26200.8246
            Мапинг в AD: operatingSystemVersion
        hardware_model(string) - модель устройства или виртуальной платформы
            Пример: Dell Latitude 5440
        serial_number(string) - серийный номер актива из биоса
        asset_tag(string) - инвентаризационный номер в организации(наклейка на корпусе)
            Пример: INV-213123
        location(string) - физическое местоположение устройства
            Пример: DC-Moscow-01,OF-Moscow-07
            Мапинг в AD: location
        status(string) - статус устройства(Активен,Остановлено,Ожидает действий),флаги на 0x2 значит отключен.
            Мапинг в AD: userAccountControl
        cpu_count(int) - кол-во физических ядер
        ram_gb(int) - общий объем оперативной памяти в ГБ
        description(string) - описание актива
            Мапинг в AD: description
        added_timestamp(datetime) - дата добавления актива
            Мапинг в AD: whenCreated
    """
    def __init__(self):
        pass