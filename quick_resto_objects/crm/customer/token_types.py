from enum import Enum


class TokenType(Enum):
    NONE = "NONE"
    PIN = "pin"
    CARD = "card"
    PHONE = "phone"
    QR_GUEST = "qrGuest"


class EntryType(Enum):
    NONE = "NONE"
    BAR_CODE = "barCode"
    TRACK_CODE = "trackCode"
    QR_CODE = "qrCode"
    MANUAL = "manual"


StrToCrmCustomerTokenType = {
    TokenType.PIN.value: TokenType.PIN,
    TokenType.CARD.value: TokenType.CARD,
    TokenType.PHONE.value: TokenType.PHONE,
    TokenType.QR_GUEST.value: TokenType.QR_GUEST
}

StrToCrmCustomerEntryType = {
    EntryType.BAR_CODE.value: EntryType.BAR_CODE,
    EntryType.TRACK_CODE.value: EntryType.TRACK_CODE,
    EntryType.QR_CODE.value: EntryType.QR_CODE,
    EntryType.MANUAL.value: EntryType.MANUAL
}


def convert_str_to_crm_token_type(crm_token_type: str) -> TokenType:
    crm_token_type = crm_token_type.upper()

    if crm_token_type in TokenType.__members__.keys():
        return TokenType.__members__[crm_token_type]

    return TokenType.NONE


def convert_str_to_crm_entry_type(crm_entry_type: str) -> EntryType:
    crm_entry_type = crm_entry_type.upper()

    if crm_entry_type in EntryType.__members__.keys():
        return EntryType.__members__[crm_entry_type]

    return EntryType.NONE
