FROM node:14
# Create app directory
WORKDIR /web
# Install app dependencies
COPY package*.json ./

RUN npm install
# Copy app source code
COPY . .

CMD ["npm", "start"]
