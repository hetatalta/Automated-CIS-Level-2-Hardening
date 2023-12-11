import requests
import os
import win32com.client
from enum import Enum

# Define CIS Benchmark URLs
cis_benchmarks_url = "https://raw.githubusercontent.com/cis-community/cis-benchmarks/master/approved/"

# Define operating system types
class OS(Enum):
    WINDOWS = 1
    LINUX = 2

def get_os_type():
  """
  Returns the operating system type (Windows or Linux).
  """
  if os.name == "nt":
    return OS.WINDOWS
  else:
    return OS.LINUX

def download_cis_benchmark(os_type):
  """
  Downloads the CIS benchmark for the specified operating system type.
  """
  if os_type == OS.WINDOWS:
    benchmark_url = f"{cis_benchmarks_url}/windows/cis-microsoft-windows-server-2019-level-2.csv"
  elif os_type == OS.LINUX:
    benchmark_url = f"{cis_benchmarks_url}/linux/cis-ubuntu-linux-22.04-lts-level-2.csv"
  else:
    raise ValueError("Unsupported operating system")

  response = requests.get(benchmark_url)
  if response.status_code == 200:
    with open("cis_benchmark.csv", "wb") as f:
      f.write(response.content)
    print(f"Downloaded CIS benchmark for {os_type.name}")
  else:
    raise ValueError(f"Failed to download CIS benchmark: {response.status_code}")

def apply_cis_hardening(os_type):
  """
  Applies CIS Level 2 hardening to the system.
  """
  if os_type == OS.WINDOWS:
    from cis_hardening_windows import harden_windows
    harden_windows("cis_benchmark.csv")
  elif os_type == OS.LINUX:
    # Implement hardening logic for Linux based on CIS Level 2 benchmark
    pass
  else:
    raise ValueError("Unsupported operating system")

def main():
  """
  Main function that executes the script.
  """
  os_type = get_os_type()
  download_cis_benchmark(os_type)
  apply_cis_hardening(os_type)
  print("CIS Level 2 hardening applied successfully.")

if __name__ == "__main__":
  main()
