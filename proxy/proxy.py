class Base:
    def getData(self) -> dict:
        raise NotImplementedError


class Subject(Base):
    def getData(self) -> dict:
        data = {
            "GUEST": [
                {
                    "msg": "guest discount"
                }
            ],
            "MEMBER": [
                {
                    "msg": "member discount"
                },
                {
                    "msg": "member bonus"
                }
            ],
            "VIP": [
                {
                    "msg": "free of charge for one year"
                }
            ]
        }

        return data


class Auth:
    GUEST = "GUEST"
    MEMBER = "MEMBER"
    VIP = "VIP"


class SubjectProxy(Base):

    def __init__(self):
        self._subject = Subject()
        self._data = self._subject.getData()

    def setAuth(self, auth: Auth):
        self.auth = auth

    def getData(self) -> dict:

        if self.auth == Auth.GUEST:
            guestData = {k: v for k, v in self._data.items() if k ==
                         Auth.GUEST}
            return guestData

        if self.auth == Auth.MEMBER:
            memberData = {k: v for k, v in self._data.items(
            ) if k in [Auth.GUEST, Auth.MEMBER]}
            return memberData

        if self.auth == Auth.VIP:
            return self._data


if __name__ == "__main__":
    subjectProxy = SubjectProxy()

    auth = Auth.GUEST
    subjectProxy.setAuth(auth=auth)
    print(subjectProxy.getData())

    auth = Auth.MEMBER
    subjectProxy.setAuth(auth=auth)
    print(subjectProxy.getData())

    auth = Auth.VIP
    subjectProxy.setAuth(auth=auth)
    print(subjectProxy.getData())
