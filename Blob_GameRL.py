# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:17:33 2020

@author: deepa
"""

import Blob_backend
import numpy as np
import matplotlib.pyplot as plt

env=Blob_backend.BlobGame.create_game()
print(env.state)
print(env.reset())

LEARNING_RATE=0.1
DISCOUNT=0.95
EPISODES=1000
LOW_QVAL=-2

SHOW_EVERY=200

epsilon=0
START_EPSILON_DECAYING=1
END_EPSILON_DECAYING=EPISODES//2
EPSILON_DECAYS_EVERY=10
epsilon_decay_value=epsilon/(END_EPSILON_DECAYING-START_EPSILON_DECAYING)



'''DISCRETE_OS_SIZE=[40]*len(env.observation_space.high)
discrete_os_win_size=(env.observation_space.high-env.observation_space.low)/DISCRETE_OS_SIZE'''

q_table=np.random.uniform(low=LOW_QVAL,high=0,size=((env.OBS_SPACE)+[len(env.ACTION_SPACE)]))

print(q_table[tuple([0,1])+(3,)])

#print()

#print(q_table)

ep_rewards=[]
aggr_ep_rewards={'ep':[], 'avg':[], 'min':[], 'max':[]}

#discrete state = (posn,attribute)  left=0 up=1 right=2 down=3 and /0 nothing/1 food/2 enemy

def get_discrete_state(rel_state):
    if rel_state[0]==[1,0]:
        return (2,1)
    elif rel_state[0]==[-1,0]:
        return ()
        
    return 

discrete_state=get_discrete_state(env.reset())
#print()
episode_reward=0
'''render=False
for episode in range(EPISODES):
 episode_reward=0'''
'''if episode%SHOW_EVERY==0:
render=True
else:
    render=False'''
render=False
done=False
while not done:
    #if np.random.random()>epsilon:
    action=np.argmax(q_table[discrete_state])
    #else:
    #action=np.random.randint(len(env.ACTION_SPACE))
    new_state,reward,done=env.step(action)
    episode_reward+=reward
    #print(reward)

    new_discrete_state=tuple(new_state)
    if not done:
        max_future_q=np.max(q_table[new_discrete_state])
        current_q=q_table[discrete_state + (action, )]
    
        new_q= (1-LEARNING_RATE)*current_q + LEARNING_RATE * (reward+DISCOUNT*(max_future_q))
        q_table[discrete_state +(action, )]=new_q
    else:
        q_table[discrete_state+(action, )]=0
        #print(f"We made it on episode {episode}")
    if render==True:
        #print(episode)
        env.render()
    
    '''if END_EPSILON_DECAYING>=episode>=START_EPSILON_DECAYING:
        epsilon-=epsilon_decay_value
ep_rewards.append(episode_reward)
if episode%SHOW_EVERY==0:
    average_reward=sum(ep_rewards[-SHOW_EVERY:])/len(ep_rewards[-SHOW_EVERY:])
    aggr_ep_rewards['ep'].append(episode)
    aggr_ep_rewards['avg'].append(average_reward)
    aggr_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))
    aggr_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))
        
        print(f"Episode:{episode} avg:{average_reward} min {min(ep_rewards[-SHOW_EVERY:])} max {max(ep_rewards[-SHOW_EVERY:])}")'''
#env.close()
    
    
'''plt.plot(aggr_ep_rewards['ep'],aggr_ep_rewards['avg'],label='avg')
plt.plot(aggr_ep_rewards['ep'],aggr_ep_rewards['max'],label='max')
plt.plot(aggr_ep_rewards['ep'],aggr_ep_rewards['min'],label='min')
plt.legend(loc=4)
plt.show()'''








