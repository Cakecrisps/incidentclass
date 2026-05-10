class AdUserAccount:
    """
    account_name(string) - логин пользователья в системе
        Пример: mskdc1adm
        Мапинг в AD: sAMAccountName
    responsible(string) - отдел или сотрудник отвественный за учетку
        Пример: msksoc1, фио
        Мапинг в AD:  manager
    email(string) - рабочая почта отвественного
        Мапинг в AD: mail
    department(string) - департамент или отдел responsible
        Мапинг в AD: Либо через юниты,либо через department
    account_type(string) - тип аккаунта(User,Service,Admin,Shared)
    status(string) - статус учетной записи(Active,Disabled,Locked)
        Мапинг в AD: userAccountControl(0x2 - отключен)
    password_last_set(datetime) - время последней смены пароля(нужно чтобы контролировать парольные политики)
        Мапинг в AD: pwdLastSet
    2fa(bool) - включени ли 2fa
    sid(string) - уникальный идентефикатор безопасности
        Пример: S-1-5-21-3904477130-2543200605-1108020080-1001
        Мапинг в AD: objectSid
    account_scope(string) - область действия учетной записи(Domain,Local)
        Мапинг в AD:Локальные учетные записи вообще не попадают в AD
    associated_host(string) - имя хоста(только для Local)
        Пример: desktop-qtnajcd
    organization(string) - организация к которой относится хост
        Мапинг в AD: Либо через юниты,либо через o/company
    """