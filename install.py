import os
import sys
import venv
import platform
import subprocess
from pathlib import Path

def run_command(command):
    """Run a command and return its success status"""
    try:
        print(f"Running: {' '.join(command)}")
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return False

def setup_environment():
    """Set up everything needed for the calculator project"""
    project_dir = Path(__file__).parent
    venv_dir = project_dir / "venv"
    
    print("=== Calculator Setup Script ===\n")
    
    # 1. Create virtual environment if it doesn't exist
    if not venv_dir.exists():
        print("Creating virtual environment...")
        venv.create(venv_dir, with_pip=True)
        print("Virtual environment created!")
    
    # 2. Set up paths
    if sys.platform == "win32":
        python_path = venv_dir / "Scripts" / "python"
        pip_path = venv_dir / "Scripts" / "pip"
        activate_cmd = "venv\\Scripts\\activate"
    else:
        python_path = venv_dir / "bin" / "python"
        pip_path = venv_dir / "bin" / "pip"
        activate_cmd = "source venv/bin/activate"
    
    python_path = str(python_path)
    pip_path = str(pip_path)
    
    # 3. Check and install tkinter if needed
    if platform.system() == "Linux":
        try:
            import tkinter
            print("Tkinter is already installed")
        except ImportError:
            print("Installing tkinter...")
            if os.path.exists("/usr/bin/apt"):
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
    
    # 4. Upgrade pip and install setuptools
    print("\nUpgrading pip and installing setuptools...")
    run_command([pip_path, "install", "--upgrade", "pip"])
    run_command([pip_path, "install", "--upgrade", "setuptools", "wheel"])
    
    # 5. Install the calculator package
    print("\nInstalling calculator package...")
    run_command([python_path, "setup.py", "develop"])
    
    print("\n=== Setup Complete! ===")
    print(f"\nTo use the calculator:")
    print(f"1. Activate the virtual environment:")
    print(f"   {activate_cmd}")
    print("2. Run the calculator:")
    print("   python -m calculator")

if __name__ == "__main__":
    setup_environment()
