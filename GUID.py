import uuid

#

namespace = uuid.NAMESPACE_URL
name = 'example.net'

#

uuid.getnode()  # MACアドレスを取得

print(uuid.uuid1())  # ホスト名と現在時刻から生成

print(uuid.uuid3(namespace, name))  # UUIDと名前のMD5ハッシュから生成

print(uuid.uuid4())  # ランダムに生成（セキュア）

print(uuid.uuid5(namespace, name))  # UUIDと名前のSHA-1ハッシュから生成

# uuid.uuid3()とuuid.uuid5()のnamespace(UUID)には以下のいずれかの定数を用いる
uuid.NAMESPACE_DNS  # nameは完全修飾ドメイン名
uuid.NAMESPACE_URL  # nameはURL
uuid.NAMESPACE_OID  # nameはISO OID
uuid.NAMESPACE_X500  # nameはX.500 DNのDERまたはテキスト出力形式

#

guid = uuid.uuid4()
str(guid)  # 16進数文字列を生成
# '25ea34da-cb04-4928-8f2c-ac0a5d5bfcc9'

guid.bytes  # 16byteの値を生成
# b'%\xea4\xda\xcb\x04I(\x8f,\xac\n][\xfc\xc9'

uuid.UUID(bytes=guid.bytes)  # UUID文字列からUUIDを生成
# UUID('25ea34da-cb04-4928-8f2c-ac0a5d5bfcc9')
