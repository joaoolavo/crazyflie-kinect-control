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
#include "vicon_t/vicon_pos_t.hpp"
#include "crazyflie_t/crazyflie_imu_t.hpp"
float pos[3], roll, pitch, yaw, timestamp, t = 0;


class Handler 
{
    public:
        ~Handler() {}

        void handleMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const vicon_t::vicon_pos_t* msg)
        {   
            pos[0] = msg->q[0];
            pos[1] = msg->q[1];          
            pos[2] = msg->q[2];
            
            printf("Received message on channel \"%s\":\n", chan.c_str());
            printf("  timestamp   = %lld\n", (long long)msg->timestamp);
            printf("  position    = (%f, %f, %f)\n",
                    msg->q[0], msg->q[1], msg->q[2]);           
            //printf("  enabled     = %d\n", msg->enabled);
            
            
            
        }
};

int main(int argc, char** argv)
{
    lcm::LCM lcm;

    if(!(lcm.good()))
        return 1;

    Handler handlerObject;

    lcm.subscribe("cf2_pete1", &Handler::handleMessage, &handlerObject);
    while(0 == lcm.handle());

    return 0;
}

