

1. **Copy files from the container to a location within WSL 2**:
   - Use `docker cp` to copy the files from the container to a location within your WSL 2 file system.

     ```bash
     docker cp dash:/app/data /mnt/c/Users/sawal/OneDrive/Bureau/Ops
     ```

   This command will copy the contents of the `/app/data` directory from the "dash" container to a directory within your WSL 2 file system.

2. **Access the copied files in WSL 2**:
   - Now, navigate to the directory where you copied the files within your WSL 2 environment.

     ```bash
     cd /mnt/c/Users/sawal/OneDrive/Bureau/Ops
     ```

3. **Copy the files to the desired Windows location**:
   - Once you're in the directory containing the copied files, you can use regular Linux commands to copy them to any Windows-accessible location.

     ```bash
     cp -r . /mnt/c/Users/sawal/OneDrive/Bureau/Ops
     ```

   This command will recursively copy all files and directories from the current directory to `C:\Users\sawal\OneDrive\Bureau\Ops` on your Windows file system.

By following these steps, you can effectively copy files from a Docker container running in WSL 2 to a location on your Windows file system.