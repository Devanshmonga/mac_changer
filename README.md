# mac_changer
allows you to  change your mac adress in 1 command , simple and easy to use  


Below is a GitHub-ready description (README) for your MAC address changer project:

---

# MAC Address Changer

**MAC Address Changer** is a lightweight Python tool that allows users to change the MAC address of a specified network interface easily using command-line arguments. This script is especially useful for network testing, privacy improvements, and troubleshooting network issues on Linux systems.

## Features

- **Current MAC Address Retrieval:** Automatically fetches and displays the current MAC address of the specified network interface.
- **MAC Address Modification:** Changes the MAC address to a user-specified value by temporarily disabling the network interface, applying the update, and re-enabling it.
- **Robust Argument Parsing:** Uses the `optparse` module to ensure that both the network interface and new MAC address are provided.
- **Easy to Use:** A straightforward script with clear output messages for easy debugging and tracking of changes.

## Requirements

- **Python 3.x**  
- **Linux Environment:** The script leverages `ifconfig`, which is common on Unix-based systems.
- **Administrative Privileges:** You may need to run the script with `sudo` to ensure proper permissions to change network configurations.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<yourusername>/mac-address-changer.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd mac-address-changer
   ```

3. **Run the script:**

   Ensure that you supply both the network interface and the new MAC address. For example:

   ```bash
   sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55
   ```

   This command sets the MAC address for the `eth0` interface to `00:11:22:33:44:55`.

## How It Works

- The script first uses the `optparse` module to capture command-line options. If either the interface or the MAC address is missing, it displays an error prompting for complete input.
- It then retrieves the current MAC address by parsing the output of the `ifconfig` command with a regular expression.
- To change the MAC address, the script:
  - Brings the specified network interface down.
  - Configures the interface with the new MAC address.
  - Brings the interface back up.
- Finally, it verifies whether the change was successful and prints corresponding messages.

## Disclaimer

Changing your MAC address might affect your network connectivity and could violate network policies. This tool is intended for educational purposes and network testing on systems you authorize. Use it responsibly.

## Contributing

Contributions are welcome! If you have ideas to enhance this project or want to improve the code, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions, feedback, or suggestions, please open an issue on GitHub or contact the repository maintainer.

---

*For further exploration, consider adding features such as support for different network configuration utilities or a more robust input validation framework. Happy coding!*
