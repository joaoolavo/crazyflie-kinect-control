// file: listener.cpp
//
// LCM example program.
//
// compile with:
//  $ g++ -o listener listener.cpp -llcm
//
// On a system with pkg-config, you can also use:
//  $ g++ -o listener listener.cpp `pkg-config --cflags --libs lcm`

#include <stdio.h>

#include <lcm/lcm-cpp.hpp>
#include "exlcm/example_t.hpp"
#include "exlcm/angle_t.hpp"

float pos[3], roll, pitch, yaw, thrust;

class Handler 
{
    public:
        ~Handler() {}

        void handleMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const exlcm::example_t* msg)
        {
            pos[0] = msg->position[0];
            pos[1] = msg->position[1];          
            pos[2] = msg->position[2];
            /*
            printf("Received message on channel \"%s\":\n", chan.c_str());
            printf("  timestamp   = %lld\n", (long long)msg->timestamp);
            printf("  position    = (%f, %f, %f)\n",
                    msg->position[0], msg->position[1], msg->position[2]);
            
            printf("  enabled     = %d\n", msg->enabled);
            */
            //thrust = 0.03*9.81 + 
        }
};

class Handler1 
{
    public:
        ~Handler1() {}

        void handleMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const exlcm::angle_t* msg)
        {
            roll = msg->roll;
            pitch = msg->pitch;
            yaw = msg->yaw;
            /*
            printf("Received message on channel \"%s\":\n", chan.c_str());
            printf("  timestamp   = %lld\n", (long long)msg->timestamp);
            printf("  angulos   = (%f, %f, %f)\n",
                    msg->roll, msg->pitch, msg->yaw);
            
            printf("  enabled     = %d\n", msg->enabled);
            */
        }
};

int main(int argc, char** argv)
{
    lcm::LCM lcm;

    if(!(lcm.good()))
        return 1;

    Handler handlerObject;
    Handler1 handlerObject1;
    lcm.subscribe("ANG_CF", &Handler1::handleMessage, &handlerObject1);
    lcm.subscribe("POS_CF", &Handler::handleMessage, &handlerObject);
    
    while(0 == lcm.handle());

    return 0;
}
