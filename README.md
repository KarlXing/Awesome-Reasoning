# Awesome-Reasoning
This is an ongoing list of papers about different categories of reasoning. I added some personal understanding for most of them, but feel free the check out the [cleaned version](https://github.com/KarlXing/Awesome-Reasoning/blob/master/README_CLEAN.md).


## Basics And Theoretical Work
1. Keyulu Xu, Jingling Li, Mozhi Zhang, Simon S. Du, Ken-ichi Kawarabayashi, & Stefanie Jegelka (2020). What Can Neural Networks Reason About?. In International Conference on Learning Representations. [[pdf]](https://arxiv.org/abs/1905.13211#:~:text=Neural%20networks%20have%20succeeded%20in,but%20less%20structured%20networks%20fail.)  
  **Key Points**: The structure of neural networks should align with underlying reasoning process of tasks for better generalization. (BTW, GNN is powerful in reasoning) 
  
2. van Steenkiste, S., Locatello, F., Schmidhuber, J., & Bachem, O. (2019). Are Disentangled Representations Helpful for Abstract Visual Reasoning?. In Advances in Neural Information Processing Systems (pp. 14222-14235). [[pdf]](https://arxiv.org/abs/1905.12506)  
  **Key Points**: Disentanglement helps improve learning efficiency of downstream reasoning tasks. A very large-scale study with some useful conclusions.
  
  


## Visual Reasoning
1. Mao, J., Gan, C., Kohli, P., Tenenbaum, J., & Wu, J. (2019). The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision. In International Conference on Learning Representations. [[pdf]](https://arxiv.org/abs/1904.12584)     
 **Dataset**: CLEVR & VQS;  
 **Key Points**: Learning visual concepts and sentence semantic parsing jointly with only image and QA pairs.
 



## Abstract Reasoning
1. Zheng, K., Zha, Z. J., & Wei, W. (2019). Abstract Reasoning with Distracting Features. In Advances in Neural Information Processing Systems (pp. 5834-5845). [[pdf]](https://papers.nips.cc/paper/8819-abstract-reasoning-with-distracting-features)   
  **Dataset**: Raven & PGM  
  **Key Points**: Distracting features have negative influence on learning reasoning tasks, but its influence could be mediated by the order of training samples. This work uses reinforcement learning to train a teacher model that makes a curriculum for a student model to learn the reasoning task.

2. Felix Hill, Adam Santoro, David Barrett, Ari Morcos, & Timothy Lillicrap (2019). Learning to Make Analogies by Contrasting Abstract Relational Structure. In International Conference on Learning Representations. [[pdf]](https://openreview.net/forum?id=SylLYsCcFm)   
  **Dataset**: From PGM  
  **Key Points**: This paper proposes LABC (learning analogy by contrasting) which means selecting incorrect candidate answers that have similar perceptual properties as the correct answer to force the learner to learn to infer analogical relations rather than perceptural correlations.
  
3. Steenbrugge, X., Leroux, S., Verbelen, T., & Dhoedt, B. (2018). Improving generalization for abstract reasoning tasks using disentangled feature representations. arXiv preprint arXiv:1811.04784. [[pdf]](https://arxiv.org/abs/1811.04784)      
  **Key Points**: A simplified version of *Are Disentangled Representations Helpful for Abstract Visual Reasoning*. Gradually increasing beta value during vae training seems interesting.


4. Zhang, C., Jia, B., Gao, F., Zhu, Y., Lu, H., & Zhu, S. C. (2019). Learning perceptual inference by contrasting. In Advances in Neural Information Processing Systems (pp. 1073-1085).   [[pdf]](http://wellyzhang.github.io/attach/neurips19zhang.pdf)   
  **Key Points**: This paper uses a contrastive module that focuses on discrimiative features and a practical NCE loss. Besides that, an inference module that learns the underlying rules are trained jointly.   
  
  
5. Wang, Duo, Mateja Jamnik, and Pietro Lio (2020). Abstract diagrammatic reasoning with multiplex graph networks. In International Conference on Learning Representations. [[pdf]](https://openreview.net/forum?id=ByxQB1BKwH)  
  **Key Points**: Extract object-level representations and use multiplex graph networks to learn relation embeddings between nodes and for final reasoning. The writing is not clear for me though..

  


## Logical Reasoning
1. Dai, Wang-Zhou, et al. "Bridging Machine Learning and Logical Reasoning by Abductive Learning." Advances in Neural Information Processing Systems. 2019.  [[pdf]](https://papers.nips.cc/paper/8548-bridging-machine-learning-and-logical-reasoning-by-abductive-learning.pdf)   
  **Key Points**: The learning system is composed of a perception module that encodes sensory information into semantic concepts and a logical reasoning module that learns the logic program with semantic concepts as input. The learning for each of them is intuitive (supervised training and abductive logic programming). The question is how to bridge them. Under the ABL (Abductive Learning) framework, the key is finding a concept mapping (actually the bridge) that maximizes the number of training samples that can be satisified by the learned logic programs. This is implemented via greedy search.   



## Dataset
1. **RAVEN**  
   **Paper**: Zhang, Chi, et al. "Raven: A dataset for relational and analogical visual reasoning." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2019.  [[data]](http://wellyzhang.github.io/project/raven.html)    
   **Key Points**: Each image is generated based on a 5-level (scene, structure, component, layout and entity) grammer and attributes are associated with layouts and entities. Rules (constant, arithmetic, progression and distributed three) are applied to attributes to form an ordered triple-image sequence for inference. Personally, I recommend to check the supplementary for a more intuitive understanding about the dataset.

2. **PGM**  
   **Paper**: Santoro, Adam, et al. "Measuring abstract reasoning in neural networks." International Conference on Machine Learning. 2018. [[data]](https://github.com/deepmind/abstract-reasoning-matrices)   
   **Key Points**: The first work that proposed reasoning dataset based on Raven's Progressive Matrices. Compared to RAVEN, it's less diverse but has more design on data splitting for generalization. 


3. **PHYRE**  
   **Paper**: Bakhtin, A., van der Maaten, L., Johnson, J., Gustafson, L., & Girshick, R. (2019). Phyre: A new benchmark for physical reasoning. In Advances in Neural Information Processing Systems (pp. 5083-5094). [[data]](https://phyre.ai/)      
   **Key Points**: A physical reasoning benchmark based on deterministic Newtonion physics with three forces (gravity, friction, collision) taken into consideration. Each task is composed of balls and rectangle bars. The goal is placing one (PHERE-B) or two (PHERE-2B) balls so that the goal object could touch the goal subject for 3 seconds.   
