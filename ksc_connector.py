class ksc_connector:
    """
    API endpoint: POST https://<ksc_host>:13299/api/v1.0/<Method>
    Основной метод поиска хостов: HostGroup.FindHosts + ChunkAccessor.GetItemsChunk
    Результат итерируется постранично через strAccessor токен.
 
    Attributes:
 
        host — данные об управляемом устройстве (сущность Assets):
 
            assets_name(string) — отображаемое имя хоста в KSC
                KSC: KLHST_WKS_DN
 
            domain_name(string) — FQDN хоста
                KSC: KLHST_WKS_FQDN
 
            dns_name(string) — имя хоста без DNS суффикса
                KSC: KLHST_WKS_DNSNAME
 
            dns_domain(string) — DNS суффикс (домен)
                KSC: KLHST_WKS_DNSDOMAIN
 
            ip(string) — IP адрес хоста
                KSC: ipAddress
 
            ksc_host_guid(string) — уникальный GUID хоста в KSC, используется как ключ для всех доп. запросов
                KSC: KLHST_WKS_HOSTNAME
 
            ksc_instance_id(string) — идентификатор экземпляра агента
                KSC: KLHST_INSTANCEID
 
            os_name(string) — название операционной системы
                Пример: Microsoft Windows 10 Pro
                KSC: KLHST_WKS_OS_NAME
 
            os_build(string) — номер сборки ОС
                Пример: 19045
                KSC: KLHST_WKS_OS_BUILD_NUMBER
 
            hardware_model(string) — тип устройства, расшифровка битовой маски CTYPE
                Пример: Workstation, Server, Laptop
                KSC: KLHST_WKS_CTYPE
 
            is_virtual(bool) — является ли устройство виртуальной машиной
                KSC: HST_VM_TYPE (0 = физическое, иначе VM)
 
            vm_type(string) — тип виртуализации
                Пример: VMware, Hyper-V, VirtualBox
                KSC: HST_VM_TYPE
 
            mac_address(string) — MAC адрес сетевого интерфейса
                KSC: HWInvStorageSrvViewName -> поле MAC
 
            serial_number(string) — серийный номер устройства из BIOS
                KSC: HWInvStorageSrvViewName -> поле SerialNumber
 
            asset_tag(string) — инвентаризационный номер (наклейка)
                KSC: HWInvStorageSrvViewName -> поле InvNum
 
            location(string) — адрес агента сетевого агента
                Пример: http://10.2.0.28:15000
                KSC: KLHST_LOCATION
 
            status(int) — битовая маска статуса хоста
                0x1  = агент онлайн
                0x2  = есть критические события
                0x4  = устаревшие антивирусные базы
                0x10 = антивирус установлен
                KSC: KLHST_WKS_STATUS
 
            added_timestamp(datetime) — дата добавления хоста в KSC
                KSC: KLHST_WKS_CREATED
 
            last_seen(datetime) — время последнего подключения агента к серверу
                KSC: KLHST_WKS_LAST_NAGENT_CONNECTED
 
            last_scan(datetime) — время последней полной антивирусной проверки
                KSC: KLHST_WKS_LAST_FULLSCAN
 
            last_update(datetime) — время последнего обновления баз/агента
                KSC: KLHST_WKS_LAST_INFOUDATE
 
            last_boot(datetime) — время последней загрузки ОС
                KSC: KLHST_WKS_LAST_SYSTEM_START
 
            reboot_required(bool) — требуется ли перезагрузка
                Актуально после патчинга при реагировании на инцидент
                KSC: KLHST_WKS_RBT_REQUIRED
 
            av_bases_date(datetime) — дата актуальных антивирусных баз
                KSC: KLHST_WKS_RTP_AV_BASES_TIME
 
            av_version(string) — версия антивирусного движка
                KSC: KLHST_WKS_RTP_AV_VERSION
 
            rtp_state(int) — состояние защиты в реальном времени
                0 = отключена, 1 = включена, иные значения = ошибка
                KSC: KLHST_WKS_RTP_STATE
 
            edr_status(int) — статус компонента EDR
                0 = не установлен / не активен
                KSC: KLHST_WKS_EDR_STATUS
 
            virus_count(int) — количество обнаруженных угроз за период
                KSC: KLHST_WKS_VIRUS_COUNT
 
            description(string) — описание хоста
                KSC: KLHST_WKS_COMMENT
 
        user — данные о пользователе, залогиненном на хосте (сущность AdUserAccount):

            sid(string) - SID пользователя:
                KSC: ul_imgSid
 
            account_name(string) — логин пользователя
                KSC: KLSPL_USER_NAME
 
            full_name(string) — полное имя пользователя
                KSC: KLSPL_USER_FULL_NAME
 
            email(string) — почта пользователя
                KSC: KLSPL_USER_MAIL
 
            status(bool) — активна ли учётная запись
                KSC: KLSPL_USER_ENABLED
 
            description(string) — описание учётной записи
                KSC: KLSPL_USER_DESCRIPTION
 
        vuln — данные об уязвимостях на хосте из модуля VAPM (сущности Vuln):
 
            vuln_id(string) — идентификатор уязвимости в KSC
                KSC: VAPM -> vuln_id
 
            cve_id(string) — идентификатор в международном реестре CVE
                Пример: CVE-2023-38831
                KSC: VAPM -> cve_id
 
            cvssv3(float) — оценка критичности по CVSS v3
                KSC: VAPM -> severity_v3
 
            cvssv2(float) — оценка критичности по CVSS v2
                KSC: VAPM -> severity_v2
 
            soft(string) — продукт, в котором обнаружена уязвимость
                Пример: WinRAR 6.22
                KSC: VAPM -> product_name + product_version
 
            detect_timestamp(datetime) — дата обнаружения уязвимости сканером
                KSC: VAPM -> detect_date
 
            patch_available(bool) — доступен ли патч для устранения
                KSC: VAPM -> patch_available
 
            remediation(string) — рекомендации по устранению из KSC
                KSC: VAPM -> fix_info
 
    """