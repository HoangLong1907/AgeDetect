from tensorflow.keras.callbacks import ModelCheckpoint
import tensorflow as tf

fle_s=r'C:\Users\Admin\Desktop\New folder\New folder\Nhap\Age_sex_detection.h5'
checkpointer = ModelCheckpoint(fle_s, monitor='val_loss',verbose=1,save_best_only=True,save_weights_only=False, mode='auto',save_freq='epoch')
Early_stop=tf.keras.callbacks.EarlyStopping(patience=75, monitor='val_loss',restore_best_weights=True),
callback_list=[checkpointer,Early_stop]