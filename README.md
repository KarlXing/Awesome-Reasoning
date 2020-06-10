# Awesome-Reasoning

## Basics And Theorical Work
1. Keyulu Xu, Jingling Li, Mozhi Zhang, Simon S. Du, Ken-ichi Kawarabayashi, & Stefanie Jegelka (2020). What Can Neural Networks Reason About?. In International Conference on Learning Representations.
  **Key points**: The structure of neural networks should align with underlying reasoning process of tasks for better generalization. (BTW, GNN is powerful in reasoning)


## Visual Reasoning
1. Mao, J., Gan, C., Kohli, P., Tenenbaum, J., & Wu, J. (2019). The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision. In International Conference on Learning Representations.  
 **Dataset**: CLEVR & VQS;  
 **Key points**: Learning visual concepts and sentence semantic parsing jointly with only image and QA pairs.
 



## Abstract Reasoning
1. Zheng, K., Zha, Z. J., & Wei, W. (2019). Abstract Reasoning with Distracting Features. In Advances in Neural Information Processing Systems (pp. 5834-5845).   
  **Dataset**: Raven & PGM  
  **Key Points**: Distracting features have negative influence on learning reasoning tasks, but its influence could be mediated by the order of training samples. This work uses reinforcement learning to train a teacher model that makes a curriculum for a student model to learn the reasoning task.


## Dataset
1. **RAVEN**  
   **Paper**: Zhang, Chi, et al. "Raven: A dataset for relational and analogical visual reasoning." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2019.  
   **Key Points**: Each image is generated based on a 5-level (scene, structure, component, layout and entity) grammer and attributes are associated with layouts and entities. Rules (constant, arithmetic, progression and distributed three) are applied to attributes to form an ordered triple-image sequence for inference. Personally, I recommend to check the supplementary for a more intuitive understanding about the dataset.

2. **PGM**  
   **Paper**: Santoro, Adam, et al. "Measuring abstract reasoning in neural networks." International Conference on Machine Learning. 2018.  
   **Key Points**: The first work that proposed reasoning dataset based on Raven's Progressive Matrices. Compared to RAVEN, it's less diverse but has more design on data splitting for generalization. 
