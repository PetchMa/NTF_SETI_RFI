import numpy as np
import pylab as plt

class NTF(object):

    def __init__(self):
        super().__init__()

    def random_initialization(A,rank):
        number_of_documents = A.shape[0]
        number_of_terms = A.shape[1]
        W = np.random.uniform(1,2,(number_of_documents,rank))
        H = np.random.uniform(1,2,(rank,number_of_terms))
        return W,H

    def nndsvd_initialization(A,rank):
        u,s,v=np.linalg.svd(A,full_matrices=False)
        v=v.T
        w=np.zeros((A.shape[0],rank))
        h=np.zeros((rank,A.shape[1]))

        w[:,0]=np.sqrt(s[0])*np.abs(u[:,0])
        h[0,:]=np.sqrt(s[0])*np.abs(v[:,0].T)

        for i in range(1,rank):
            
            ui=u[:,i]
            vi=v[:,i]
            ui_pos=(ui>=0)*ui
            ui_neg=(ui<0)*-ui
            vi_pos=(vi>=0)*vi
            vi_neg=(vi<0)*-vi
            
            ui_pos_norm=np.linalg.norm(ui_pos,2)
            ui_neg_norm=np.linalg.norm(ui_neg,2)
            vi_pos_norm=np.linalg.norm(vi_pos,2)
            vi_neg_norm=np.linalg.norm(vi_neg,2)
            
            norm_pos=ui_pos_norm*vi_pos_norm
            norm_neg=ui_neg_norm*vi_neg_norm
            
            if norm_pos>=norm_neg:
                w[:,i]=np.sqrt(s[i]*norm_pos)/ui_pos_norm*ui_pos
                h[i,:]=np.sqrt(s[i]*norm_pos)/vi_pos_norm*vi_pos.T
            else:
                w[:,i]=np.sqrt(s[i]*norm_neg)/ui_neg_norm*ui_neg
                h[i,:]=np.sqrt(s[i]*norm_neg)/vi_neg_norm*vi_neg.T

        return w,h
    def mu_method(A,k,W,H,max_iter,init_mode='random', save = False):
        e = 1.0e-10
        for n in range(max_iter):
            # Update H
            W_TA = W.T@A
            W_TWH = W.T@W@H+e
            for i in range(np.size(H, 0)):
                for j in range(np.size(H, 1)):
                    H[i, j] = H[i, j] * W_TA[i, j] / W_TWH[i, j]
            # Update W
            AH_T = A@H.T
            WHH_T =  W@H@H.T+ e

            for i in range(np.size(W, 0)):
                for j in range(np.size(W, 1)):
                    W[i, j] = W[i, j] * AH_T[i, j] / WHH_T[i, j]
            if n%5==0 and save:
              f, axarr = plt.subplots(1,4, figsize=(25,60))
              axarr[0].imshow(A)
              axarr[1].imshow(W@H)
              axarr[2].imshow(W)
              # axarr[2].set_aspect('auto')
              axarr[3].imshow(H)
              f.savefig("/content/drive/My Drive/Deeplearning/factoring/combined/Matrix_approx_"+str(n)+".PNG", bbox_inches='tight')
            norm = np.linalg.norm(A - W@H, 'fro')
            if n%30==0:
                print("Update Loss -- "+str(n)+" ---- "+str(norm))
            
            
        return W ,H 