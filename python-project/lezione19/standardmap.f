      !=================================================
      ! Funzione di main ausiliaria per eventuale debug
      !=================================================
      ! program main
      !     integer              :: s = 100000
      !     real*8               :: a0 = 0.1
      !     real*8               :: x0 = 0.1
      !     real*8               :: y0 = 0.1
      !     call henonmap(s, x0, y0, a0)
      ! end

      ! Per rendere eseguibile in python lanciare il comando (unix):
      ! f2py -c -m maps standardmap.f --fcompiler=gnu95

      subroutine standardmap(n, q, p, k)
      !========================================
      ! Funzione che crea la mappa standard 
      ! dati i parametri iniziali, restituisce  
      ! gli array contenenti le x e le y.
      !========================================
          integer                 :: i
          ! Definisco un pi preciso
          real*8                  :: pi = 4.d0*datan(1.d0)
          integer, intent(in)     :: n ! Numero di iterate da fare
          real*8, intent(in)      :: k ! Costante della mappa
          real*8, intent(inout)   :: q(n)
          real*8, intent(inout)   :: p(n)
          do i = 1, size(q)-1
              p(i+1) = mod(p(i) + k/(2*pi) * dsin(2 * pi * q(i)), 1.d0 )
              q(i+1) = mod(q(i) + p(i+1), 1.d0 )
          enddo
      end subroutine
