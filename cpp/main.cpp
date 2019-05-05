#include <iostream>
#include <filesystem>
#include <regex>
#include <fstream>

void process_file(std::filesystem::path file, std::ofstream& out, std::regex& re) {
	std::cout << "file: " << file << std::endl;
	out << "file: " << file << std::endl;
	std::ifstream in(file);
	std::string line;
	while (std::getline(in, line)) {
		auto str_begin = std::sregex_token_iterator(line.begin(), line.end(), re, 1);
		auto str_end = std::sregex_token_iterator();
		for (auto i = str_begin; i != str_end; ++i) {
			out << i->str() << std::endl;
			std::cout << i->str() << std::endl;
		}
	}
	in.close();
}

int main(int argc, const char* argv[])
{
	std::regex re{ R"d(fmt.Errorf\("(.+)")d" };
	std::ofstream out("str.txt");
	for (auto entry : std::filesystem::recursive_directory_iterator(std::filesystem::path("G:/devsrc/little_games/server_go/src/ateam/room"))) {
		auto path = entry.path();
		if (std::filesystem::is_regular_file(path) && path.extension() == ".go") {
			process_file(path, out, re);
		}
	}
	out.close();
	//std::cin.get();
	return 0;
}