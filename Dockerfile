# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt (if you have dependencies) to the working directory
COPY ./requirements.txt /app/requirements.txt

# Step 4: Install any dependencies in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Step 5: Copy the entire FastAPI app to the container
COPY . /app

# Step 6: Expose port 8000 to be able to access FastAPI app
EXPOSE 8000

# Step 7: Run the FastAPI app using Uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
