#include <stdio.h>
#include <uuid/uuid.h>
 
int main(){
 
        uuid_t uuid;
        char uuid_str[37];
 
        uuid_generate_random(uuid);
        uuid_unparse(uuid, uuid_str);
 
        printf("uuid: %s\n", uuid_str);
 
}