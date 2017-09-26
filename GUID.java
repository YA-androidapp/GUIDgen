import java.util.UUID;

public class UUIDUtil {
    public static String getUuid() {
        final UUID uuid = UUID.randomUUID();
        final String randomUUIDString = uuid.toString();

        return randomUUIDString;
    }
}