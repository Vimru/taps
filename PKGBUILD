# Maintainer: Joe Dillon <josephd31415@gmail.com>
pkgname=taps
pkgver=1.0
pkgrel=1
pkgdesc="Identify packages with vulnerable dependencies."
arch=('any')
depends=('arch-audit>=0.1.5')
license=('GPL3')
url="https://github.com/Vimru/taps"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Vimru/taps/archive/${pkgver}.tar.gz")
sha256sums=('ea6487880bacf09087987fa9b50699a3c9761425e2d2f103383ae3875d5ea691')

package() {
	install -m755 -Dt "$pkgdir/usr/bin" "$srcdir/taps-$pkgver/taps"
}
