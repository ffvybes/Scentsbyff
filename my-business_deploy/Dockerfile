# Use Nginx to serve static web files
FROM nginx:alpine

# Copy website files into nginx directory
COPY ./web /usr/share/nginx/html

# Expose port 8080
EXPOSE 8080

CMD ["ngnix", "-g", "daemon off;" ]