model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(X, Y, batch_size=4, epochs=100, 
          validation_data=(X_test, Y_test))

model.save_weights('saved.weights')
model.save('saved.model')
