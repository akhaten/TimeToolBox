{pkgs ? import <nixpkgs> { inherit system; } }:

pkgs.python310Packages.buildPythonPackage {
	name = "TimeToolBox";
	src = ./.;
	propagatedBuildInputs = with pkgs; [
		python310
		python310
        python310Packages.graphviz
	];
	doCheck = false;
}



