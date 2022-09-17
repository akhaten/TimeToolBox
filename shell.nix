let 
  
  pkgs = import <nixpkgs> {
    overlays = [

      (self: super: {

        python310Packages.pip = super.python310Packages.pip.overrideAttrs (
          old : {
            src = super.fetchFromGitHub {
              owner = "pypa";
              repo = "pip";
              rev = "22.2.2";
              sha256 = "SLjmxFUFmvgy8E8kxfc6lxxCRo+GN4L77pqkWkRR8aE=";
            };
          }
        );

      })

    ];
  };

in
pkgs.mkShell {

  allowBroken = true;

  buildInputs = with pkgs; [
    python310
    python310Packages.pip
    graphviz
  ];

  shellHook = ''
    export PIP_PREFIX=$(pwd)/env
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python310.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    unset SOURCE_DATE_EPOCH
  '';
  #export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.qt5.full}/lib:${pkgs.libGL}/lib


}