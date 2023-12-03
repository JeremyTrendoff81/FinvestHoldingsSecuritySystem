from models.User import User
from models.Role import Role

def initDemoUsers() -> list:
    userList = []

    mischa_lowery = User("mischa", "Mischa Lowery", Role.CLIENT)
    userList.append(mischa_lowery)

    veronica_perez = User("veronica", "Veronica Perez", Role.CLIENT)
    userList.append(veronica_perez)

    winston_callahan = User("winston", "Winston Callahan", Role.TELLER)
    userList.append(winston_callahan)

    kelan_gough = User("kelan", "Kelan Gough", Role.TELLER)
    userList.append(kelan_gough)

    nelson_wilkins = User("nelson", "Nelson Wilkins", Role.FINANCIAL_ADVISOR)
    userList.append(nelson_wilkins)

    kelsie_chang = User("kelsie", "Kelsie Chang", Role.FINANCIAL_ADVISOR)
    userList.append(kelsie_chang)

    howard_linker = User("howard", "Howard Linker", Role.COMPLIANCE_OFFICER)
    userList.append(howard_linker)

    stefania_smart = User("stefania", "Stefania Smart", Role.COMPLIANCE_OFFICER)
    userList.append(stefania_smart)

    willow_garza = User("willow", "Willow Garza", Role.PREMIUM_CLIENT)
    userList.append(willow_garza)

    nala_preston = User("nala", "Nala Preston", Role.PREMIUM_CLIENT)
    userList.append(nala_preston)

    stacy_kent = User("stacy", "Stacy Kent", Role.INVESTMENT_ANALYST)
    userList.append(stacy_kent)

    keikilana_kapahu = User("keikilana", "Keikilana Kapahu", Role.INVESTMENT_ANALYST)
    userList.append(keikilana_kapahu)

    kodi_matthews = User("kodi", "Kodi Matthews", Role.FINANCIAL_PLANNER)
    userList.append(kodi_matthews)

    malikah_wu = User("malikah", "Malikah Wu", Role.FINANCIAL_PLANNER)
    userList.append(malikah_wu)

    caroline_lopez = User("caroline", "Caroline Lopez", Role.TECHNICAL_SUPPORT)
    userList.append(caroline_lopez)

    pawel_barclay = User("pawel", "Pawel Barclay", Role.TECHNICAL_SUPPORT)
    userList.append(pawel_barclay)

    return userList

def main():
    users = initDemoUsers()

    for user in users:
        print(user.getUsername())

main()
