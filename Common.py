from enum import Enum
HEART_BEAT_INTERVAL = 5000
INITIAL_CONNECTION_TIMEOUT = 5000
CONNECTION_TIMEOUT = 20000
MAX_MESSAGE_SIZE = 5242880
SPLIT_MESSAGE_LENGTH = 8096
PROTOCOL_VERSION = 30
PROGRAM_VERSION = "Custom"

class CraftType(Enum):
    VAB = 0
    SPH = 1
    SUBASSEMBLY = 2


class ClientMessageType(Enum):
    HEARTBEAT = 0
    HANDSHAKE_RESPONSE = 1
    CHAT_MESSAGE = 2
    PLAYER_STATUS = 3
    PLAYER_COLOR = 4
    SCENARIO_DATA = 5
    KERBALS_REQUEST = 6
    KERBAL_PROTO = 7
    VESSELS_REQUEST = 8
    VESSEL_PROTO = 9
    VESSEL_UPDATE = 10
    VESSEL_REMOVE = 11
    CRAFT_LIBRARY = 12
    SCREENSHOT_LIBRARY = 13
    FLAG_SYNC = 14
    SYNC_TIME_REQUEST = 15
    PING_REQUEST = 16
    MOTD_REQUEST = 17
    WARP_CONTROL = 18
    LOCK_SYSTEM = 19
    MOD_DATA = 20
    SPLIT_MESSAGE = 21
    CONNECTION_END = 22


class ServerMessageType(Enum):
    HEARTBEAT = 0
    HANDSHAKE_CHALLANGE = 1
    HANDSHAKE_REPLY = 2
    SERVER_SETTINGS = 3
    CHAT_MESSAGE = 4
    PLAYER_STATUS = 5
    PLAYER_COLOR = 6
    PLAYER_JOIN = 7
    PLAYER_DISCONNECT = 8
    SCENARIO_DATA = 9
    KERBAL_REPLY = 10
    KERBAL_COMPLETE = 11
    VESSEL_LIST = 12
    VESSEL_PROTO = 13
    VESSEL_UPDATE = 14
    VESSEL_COMPLETE = 15
    VESSEL_REMOVE = 16
    CRAFT_LIBRARY = 17
    SCREENSHOT_LIBRARY = 18
    FLAG_SYNC = 19
    SET_SUBSPACE = 20
    SYNC_TIME_REPLY = 21
    PING_REPLY = 22
    MOTD_REPLY = 23
    WARP_CONTROL = 24
    ADMIN_SYSTEM = 25
    LOCK_SYSTEM = 26
    MOD_DATA = 27
    SPLIT_MESSAGE = 28
    CONNECTION_END = 29


class ConnectionStatus(Enum):
    DISCONNECTED = 0
    CONNECTING = 1
    CONNECTED = 2


class ClientState(Enum):
    DISCONNECTED = 0
    CONNECTING = 1
    CONNECTED = 2
    HANDSHAKING = 3
    AUTHENTICATED = 4
    TIME_SYNCING = 5
    TIME_SYNCED = 6
    SYNCING_KERBALS = 7
    KERBALS_SYNCED = 8
    SYNCING_VESSELS = 9
    VESSELS_SYNCED = 10
    TIME_LOCKING = 11
    TIME_LOCKED = 12
    STARTING = 13
    RUNNING = 14
    DISCONNECTING = 15


class WarpMode(Enum):
    MCW_FORCE = 0
    MCW_VOTE = 1
    MCW_LOWEST = 2
    SUBSPACE_SIMPLE = 3
    SUBSPACE = 4
    NONE = 5


class GameMode(Enum):
    SANDBOX = 0
    SCIENCE = 1
    CAREER = 2


class ModControlMode(Enum):
    DISABLED = 0
    ENABLED_STOP_INVALID_PART_SYNC = 1
    ENABLED_STOP_INVALID_PART_LAUNCH = 2


class WarpMessageType(Enum):
    REQUEST_VOTE = 0
    REPLY_VOTE = 1
    CHANGE_WARP = 2
    SET_CONTROLLER = 3
    NEW_SUBSPACE = 4
    CHANGE_SUBSPACE = 5
    RELOCK_SUBSPACE = 6
    REPORT_RATE = 7


class CraftMessageType(Enum):
    LIST = 0
    REQUEST_FILE = 1
    RESPOND_FILE = 2
    UPLOAD_FILE = 3
    ADD_FILE = 4
    DELETE_FILE = 5


class ScreenshotMessageType(Enum):
    NOTIFY = 0
    SEND_START_NOTIFY = 1
    WATCH = 2
    SCREENSHOT = 3


class ChatMessageType(Enum):
    LIST = 0
    JOIN = 1
    LEAVE = 2
    CHANNEL_MESSAGE = 3
    PRIVATE_MESSAGE = 4
    CONSOLE_MESSAGE = 5


class AdminMessageType(Enum):
    LIST = 0
    ADD = 1
    REMOVE = 2


class LockMessageType(Enum):
    LIST = 0
    ACQUIRE = 1
    RELEASE = 2


class FlagMessageType(Enum):
    LIST = 0
    FLAG_DATA = 1
    UPLOAD_FILE = 2
    DELETE_FILE = 3


class PlayerColorMessageType(Enum):
    LIST = 0
    SET = 1


class HandshakeReply(Enum):
    HANDSHOOK_SUCCESSFULLY = 0
    PROTOCOL_MISMATCH = 1
    ALREADY_CONNECTED = 2
    RESERVED_NAME = 3
    INVALID_KEY = 4
    PLAYER_BANNED = 5
    SERVER_FULL = 6
    NOT_WHITELISTED = 7
    INVALID_PLAYERNAME = 98
    MALFORMED_HANDSHAKE = 99


def handler(func, message_namespace):
    func.message_namespace = message_namespace + '.'
    return func


def server_network_message(func):
    return handler(func, 'ServerMessageType')


