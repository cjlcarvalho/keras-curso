model.load_weights('saved.weights')

model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

prediction = model.predict(data)
