from typing import Optional

from plugins.http_check.model.base import Model


class Section(Model):
    name: str
    DNS_Entry: Optional[str] = None,
    DNS_RecordType: Optional[str] = None,
    DNS_Server: Optional[str] = None,
    Timeout: Optional[int | float] = None,
    sev: Optional[str] = None,
    Sev: Optional[str] = None,
    DNS_Protocol: Optional[str] = "UDP",  # default UDP, optional
    DNS_Port: Optional[int] or str = 53,  # default 53, optional
    DNS_Result: Optional[str] = None,  # optional, must match result or error

