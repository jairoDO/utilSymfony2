<?php

namespace Gse\Campus2Bundle\Entity\Capacitacion;

use Symfony\Component\Validator\Constraints as Assert;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Criteria;
use Doctrine\ORM\Mapping as ORM;
use Gedmo\Mapping\Annotation as Gedmo;

use Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado;
use Gse\Campus2Bundle\Entity\TipoCapacitacion;

/**
 * @ORM\Table("campus__capacitacion_edicion")
 * @ORM\Entity(repositoryClass="Gse\Campus2Bundle\Entity\Capacitacion\EdicionRepository")
 */
class Edicion
{
    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @var \Gse\Campus2Bundle\Entity\Capacitacion
     *
     * @ORM\ManyToOne(
     *  targetEntity="Gse\Campus2Bundle\Entity\Capacitacion",
     *  inversedBy="ediciones",
     *  cascade={"persist"}
     * )
     * @ORM\JoinColumn(onDelete="CASCADE")
     * @Assert\Valid
     */
    private $capacitacion;

    /**
     * @var string
     *
     * @ORM\Column(name="numero", type="integer")
     */
    private $numero;

    /**
     * @var string
     *
     * @ORM\Column(name="presentacion", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales", "generales_noForm", "edicion_completa"})
     */
    private $presentacion;

    /**
     * @var string
     *
     * @ORM\Column(name="descripcion", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales", "generales_noForm", "edicion_completa"})
     */
    private $descripcion;

    /**
     * @var string
     *
     * @ORM\Column(name="metodologia", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales", "generales_noForm", "edicion_completa"})
     */
    private $metodologia;

    /**
     * @var string
     *
     * @ORM\Column(name="mensajeFinal", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales", "generales_noForm", "edicion_completa"})
     */
    private $mensajeFinal;

    /**
     * @var string
     *
     * @ORM\Column(name="objetivos", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales_curso", "generales_curso_noForm", "generales_posgrado", "generales_posgrado_noForm"})
     */
    private $objetivos;

    /**
     * @var string
     *
     * @ORM\Column(name="dirigidoA", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales_curso", "generales_curso_noForm", "generales_posgrado", "generales_posgrado_noForm"})
     */
    private $dirigidoA;

    /**
     * @var string
     *
     * @ORM\Column(name="perfilDelEgresado", type="text", nullable=true)
     * @Assert\NotBlank(groups={"generales_curso", "generales_curso_noForm", "generales_posgrado", "generales_posgrado_noForm"})
     */
    private $perfilDelEgresado;

    /**
     * @var ArrayCollection
     *
     * @ORM\OneToMany(
     *  targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Certificado",
     *  mappedBy="edicion",
     *  cascade={"persist", "remove"}
     * )
     * @Assert\Valid
     */
    private $certificados;

    /**
     * @var ArrayCollection
     *
     * @ORM\OneToMany(
     *  targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Modulo",
     *  mappedBy="edicion",
     *  cascade={"persist", "remove"}
     * )
     * @ORM\OrderBy({"numero" = "ASC"})
     * @Assert\Count(min="1", groups={"estructura_academica", "estructura_academica_noForm", "edicion_completa"})
     * @Assert\Valid
     */
    private $modulos;

    /**
     * @var \DateTime
     *
     * @ORM\Column(name="fechaInicio", type="datetime", nullable=true)
     * @Assert\NotBlank(groups={"estructura_academica_noForm", "edicion_completa"})
     */
    private $fechaInicio;

    /**
     * @var \DateTime
     *
     * @ORM\Column(name="fechaFin", type="datetime", nullable=true)
     * @Assert\NotBlank(groups={"estructura_academica_noForm", "edicion_completa"})
     */
    private $fechaFin;

    /**
     * @var \DateTime
     *
     * @ORM\Column(name="fechaFinPublicidad", type="date", nullable=true)
     */
    private $fechaFinPublicidad;

    /**
     * @var \DateTime
     *
     * @ORM\Column(name="fechaFinInscripcion", type="date", nullable=true)
     */
    private $fechaFinInscripcion;

    /**
     * @var integer
     *
     * @ORM\Column(name="cupoMinimo", type="smallint", nullable=true)
     * @Assert\NotBlank(groups={"condiciones", "condiciones_noForm"})
     * @Assert\Length(min="1", groups={"condiciones", "condiciones_noForm", "edicion_completa"})
     */
    private $cupoMinimo;

    /**
     * @var integer
     *
     * @ORM\Column(name="cupoMaximo", type="smallint", nullable=true)
     * @Assert\NotBlank(groups={"condiciones", "condiciones_noForm"})
     * @Assert\Length(min="1", groups={"condiciones", "condiciones_noForm", "edicion_completa"})
     */
    private $cupoMaximo;

    /**
     * @var string
     *
     * @ORM\Column(name="preciosSugeridos", type="text", nullable=true)
     * @Assert\NotBlank(groups={"condiciones", "condiciones_noForm", "edicion_completa"})
     */
    private $preciosSugeridos;

    /**
     * @var ArrayCollection
     *
     * @ORM\OneToMany(
     *  targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion\ImagenRecomendada",
     *  mappedBy="edicion",
     *  cascade={"persist", "remove"}
     * )
     * @Assert\Valid
     * @Assert\Count(max="5", groups={"imagenes", "edicion_completa"})
     */
    private $imagenesRecomendadas;

    /**
     * @var ArrayCollection
     *
     * @ORM\OneToMany(
     *  targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Aval",
     *  mappedBy="edicion",
     *  cascade={"persist", "remove"}
     * )
     * @Assert\Valid
     */
    private $avales;

    /**
     * @var ArrayCollection
     *
     * @ORM\OneToMany(
     *  targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado",
     *  mappedBy="edicion",
     *  cascade={"persist", "remove"}
     * )
     * @ORM\OrderBy({"id"="desc"})
     */
    private $estados;

    /**
     * @var \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado
     *
     * @ORM\OneToOne(targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado", cascade={"persist"})
     * @ORM\JoinColumn(onDelete="SET NULL")
     */
    private $estadoActual;

    /**
     * @var \Gse\Campus2Bundle\Entity\Capacitacion\Edicion
     *
     * @ORM\OneToOne(targetEntity="Gse\Campus2Bundle\Entity\Capacitacion\Edicion")
     * @ORM\JoinColumn(nullable=true)
     */
    private $edicionMadre;

    /**
     * @var \DateTime
     *
     * @ORM\Column(name="created", type="datetime")
     * @Gedmo\Timestampable(on="create")
     */
    private $created;

    /**
     * @var \DateTime
     *
     * @ORM\Column(name="updated", type="datetime")
     * @Gedmo\Timestampable(on="update")
     */
    private $updated;

    /**
     * @var \Gse\AppBundle\Entity\Usuario
     *
     * @ORM\ManyToOne(targetEntity="Gse\AppBundle\Entity\Usuario")
     */
    private $createdBy;

    /**
     * @var string
     *
     * @ORM\Column(name="imagen", type="string", length=90, nullable=true)
     */
    private $imagen;

    /**
     * @var \Symfony\Component\HttpFoundation\File\UploadedFile
     * @Assert\NotBlank(groups={"imagen"})
     * @Assert\Image(groups={"imagen"})
     */
    private $imagenFile;

    // CONFIGURACIÓN DE RECURSOS

    // evaluación parcial

    /**
     * Que el recurso esté habilitado quiere decir que cuando alguien intente crear una capacitación de este tipo
     * estará este recurso habilitado por defecto (se aplica a todos los recursos)
     *
     * @var boolean
     *
     * @ORM\Column(name="evaluacionParcialHabilitado", type="boolean")
     */
    private $evaluacionParcialHabilitado = false;

    /**
     * Que el recurso esté bloqueado quiere decir que el usuario que intente crear una capacitacitación de este tipo
     * no podrá sobreescribir la configuración de este recurso (se aplica a todos los recursos)
     *
     * @var boolean
     *
     * @ORM\Column(name="evaluacionParcialBloqueado", type="boolean")
     */
    private $evaluacionParcialBloqueado = false;

    /**
     * Es requerido aprobar las evaluaciones parciales para continuar con la capacitación?
     *
     * @var boolean
     *
     * @ORM\Column(name="evaluacionParcialAprobacionRequerida", type="boolean")
     */
    private $evaluacionParcialAprobacionRequerida = false;

    // trabajo práctico

    /**
     * @var boolean
     *
     * @ORM\Column(name="trabajoPracticoHabilitado", type="boolean")
     */
    private $trabajoPracticoHabilitado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="trabajoPracticoBloqueado", type="boolean")
     */
    private $trabajoPracticoBloqueado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="trabajoPracticoAprobacionRequerida", type="boolean")
     */
    private $trabajoPracticoAprobacionRequerida = false;

    // autoevaluación

    /**
     * @var boolean
     *
     * @ORM\Column(name="autoevaluacionHabilitado", type="boolean")
     */
    private $autoevaluacionHabilitado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="autoevaluacionBloqueado", type="boolean")
     */
    private $autoevaluacionBloqueado = false;

    // evaluación final

    /**
     * @var boolean
     *
     * @ORM\Column(name="evaluacionFinalHabilitado", type="boolean")
     */
    private $evaluacionFinalHabilitado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="evaluacionFinalBloqueado", type="boolean")
     */
    private $evaluacionFinalBloqueado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="evaluacionFinalAprobacionRequerida", type="boolean")
     */
    private $evaluacionFinalAprobacionRequerida = false;

    // trabajo final

    /**
     * @var boolean
     *
     * @ORM\Column(name="trabajoFinalHabilitado", type="boolean")
     */
    private $trabajoFinalHabilitado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="trabajoFinalBloqueado", type="boolean")
     */
    private $trabajoFinalBloqueado = false;

    /**
     * @var boolean
     *
     * @ORM\Column(name="trabajoFinalAprobacionRequerida", type="boolean")
     */
    private $trabajoFinalAprobacionRequerida = false;

    public function __construct()
    {
        $this->imagenesRecomendadas = new ArrayCollection();
        $this->avales = new ArrayCollection();
        $this->modulos = new ArrayCollection();
        $this->certificados = new ArrayCollection();
    }

    // --- Sobre Estados -------------------------------------------------------------------------- //

    /** @return boolean */
    public function esSoloLecturaParaCoordinador()
    {
        return ! $this->esEstadoCargando() && ! $this->esEstadoRechazado();
    }

    /** @return boolean */
    public function esEstadoCargando()
    {
        return $this->getEstadoActual()->getEstado() == Estado::CARGANDO;
    }

    /** @return boolean */
    public function esEstadoEnRevision()
    {
        return $this->getEstadoActual()->getEstado() == Estado::EN_REVISION;
    }

    /** @return boolean */
    public function esEstadoRechazado()
    {
        return $this->getEstadoActual()->getEstado() == Estado::RECHAZADO;
    }

    /** @return boolean */
    public function esEstadoEnEdicion()
    {
        return $this->getEstadoActual()->getEstado() == Estado::EN_EDICION;
    }

    /** @return boolean */
    public function esEstadoEnAdministracion()
    {
        return $this->getEstadoActual()->getEstado() == Estado::EN_ADMINISTRACION;
    }

    /** @return boolean */
    public function esEstadoPublicitando()
    {
        return $this->getEstadoActual()->getEstado() == Estado::PUBLICITANDO;
    }

    /** @return boolean     Es esta edición la Actual? */
    public function esEdicionActual()
    {
        return $this == $this->capacitacion->getEdicionActual();
    }

    public function publicitar()
    {
        if ($this->esWebinar()) {

            // fecha fin publicidad Webinar: fecha de comienzo edición
            $this->setFechaFinPublicidad($this->getFechaInicio());

            // fecha fin inscripcion Webinar: fecha de comienzo edición + 1 año
            $fechaFinInscripcion = clone $this->getFechaInicio();
            $this->setFechaFinInscripcion($fechaFinInscripcion->add(new \DateInterval('P1Y')));

        } elseif ($this->esTaller() || $this->esSimposio()) {

            // fecha fin publicidad TALLER O SIMPOSIO: fecha de comienzo edición +3 días
            $fechaFinPublicidad = clone $this->getFechaInicio();
            $this->setFechaFinPublicidad($fechaFinPublicidad->add(new \DateInterval('P3D')));

            // fecha fin inscripcion TALLER O SIMPOSIO: fecha de comienzo edición +4 días
            $fechaFinInscripcion = clone $this->getFechaInicio();
            $this->setFechaFinInscripcion($fechaFinInscripcion->add(new \DateInterval('P4D')));

        } elseif ($this->esCurso() || $this->esPosgrado()) {

            // fecha fin publicidad CURSO O POSGRADO: fecha de comienzo edición +10 días
            $fechaFinPublicidad = clone $this->getFechaInicio();
            $this->setFechaFinPublicidad($fechaFinPublicidad->add(new \DateInterval('P10D')));

            // fecha fin inscripcion CURSO O POSGRADO: fecha de fin de primer módulo -5 días. Si el primer módulo tiene menos de 5 días la fecha fin
            // de inscripcion es igual a la fecha inicio del primer módulo
            $fechaFinInscripcion = clone $this->getModulos()->first()->getFechaFin();
            $dateIntervalo = new \DateInterval('P5D');
            $dateIntervalo->invert = 1;
            $fechaFinInscripcion->add($dateIntervalo);

            if ($fechaFinInscripcion < $this->getModulos()->first()->getFechaInicio()) {
                $fechaFinInscripcion = clone $this->getModulos()->first()->getFechaInicio();
            }

            $this->setFechaFinInscripcion($fechaFinInscripcion);
        }
    }

    // --- Sobre Recursos -----------------------------------------------------------------------------  //

    /** @return boolean      Tiene la Edición algún recurso de Evaluación que se pueda Configurar? */
    public function tieneAlgunRecursoDeEvaluacionParaConfigurar()
    {
        return
            $this->tieneAlgunRecursoDeEvaluacionFinalParaConfigurar()
            || $this->tieneAlgunRecursoDeEvaluacionDeCursadoParaConfigurar();
    }

    /** @return boolean      Tiene la Edición algún recurso de Evaluación de Cursado que se pueda Configurar? */
    public function tieneAlgunRecursoDeEvaluacionDeCursadoParaConfigurar()
    {
        return ! $this->evaluacionParcialBloqueado || ! $this->trabajoPracticoBloqueado || ! $this->autoevaluacionBloqueado;
    }

    /** @return boolean      Tiene la Edición algún recurso de Evaluación Final que se pueda Configurar? */
    public function tieneAlgunRecursoDeEvaluacionFinalParaConfigurar()
    {
        return ! $this->evaluacionFinalBloqueado || ! $this->trabajoFinalBloqueado;
    }

    // --- Sobre Tipo de capacitación ---------------------------------------------------------------- //

    /** @return boolean     Es un Tipo de capacitación de un solo Módulo */
    public function esDeUnSoloModulo()
    {
        return $this->capacitacion->getTipo()->tieneUnSoloModulo();
    }

    /** @return boolean     Es un Tipo de capacitación de más de un Módulo */
    public function esDeMasDeUnModulo()
    {
        return $this->capacitacion->getTipo()->tieneMasDeUnModulo();
    }

    /** @return boolean     Es un Tipo de capacitación de una sola Asignatura */
    public function esDeUnaSolaAsignatura()
    {
        return $this->capacitacion->getTipo()->tieneUnaSolaAsignatura();
    }

    /** @return boolean     Es un Tipo de capacitación de más de una Asignatura */
    public function esDeMasDeUnaAsignatura()
    {
        return $this->capacitacion->getTipo()->tieneMasDeUnaAsignatura();
    }

    /** @return boolean     Es Webinar */
    public function esWebinar()
    {
        return TipoCapacitacion::WEBINAR === $this->capacitacion->getTipo()->getId();
    }

    /** @return boolean     Es Taller */
    public function esTaller()
    {
        return TipoCapacitacion::TALLER === $this->capacitacion->getTipo()->getId();
    }

    /** @return boolean     Es Simposio */
    public function esSimposio()
    {
        return TipoCapacitacion::SIMPOSIO === $this->capacitacion->getTipo()->getId();
    }

    /** @return boolean     Es Curso */
    public function esCurso()
    {
        return TipoCapacitacion::CURSO === $this->capacitacion->getTipo()->getId();
    }

    /** @return boolean     Es Posgrado */
    public function esPosgrado()
    {
        return TipoCapacitacion::POSGRADO === $this->capacitacion->getTipo()->getId();
    }

    // --- Sobre módulos ----------------------------------------------------------------------------- //

    /** @return Edicion\Modulo       Último módulo (persistido en DB) */
    public function getUltimoModulo()
    {
        return $this->getModulos()->matching(
            Criteria::create()
                ->Where(Criteria::expr()->neq('numero', null))
                ->orderBy(array('numero' => 'ASC'))
        )->last();
    }

    // --- Sobre Certificados ------------------------------------------------------------------------ //

    /** @return ArrayCollection     Certificados base (Entity\Certificado) ya agregados */
    public function getCertificadosBaseYaAgregados()
    {
        return $this->getCertificados()->matching(
            Criteria::create()->Where(Criteria::expr()->neq('basadoEnCertificadoBaseId', null))
        );
    }

    /** @return array       Ids de Certificados base (Entity\Certificado) ya agregados */
    public function getCertificadosBaseYaAgregadosIds()
    {
        $ids = array();

        foreach ($this->getCertificadosBaseYaAgregados() as $certificado)
            $ids[] = $certificado->getBasadoEnCertificadoBaseId();

        return $ids;
    }

    /**
     * @param boolean $incluirBasadosEnConcretos
     *
     * @return array    Ids de Certificados concreto (Entity\Capacitacion\Edicion\Certificado) ya agregados
     */
    public function getCertificadosConcretoYaAgregadosIds($incluirBasadosEnConcretos = true)
    {
        $ids = array();

        foreach ($this->getCertificados() as $certificado) {
            $ids[] = $certificado->getId();
            if ($incluirBasadosEnConcretos && $certificado->getBasadoEnCertificadoConcretoId()) {
                $ids[] = $certificado->getBasadoEnCertificadoConcretoId();
            }
        }

        return $ids;
    }

    // --- Imagen ------------------------------------------------------------------------------------ //

    public function uploadImagen()
    {
        if (null === $this->imagenFile) {
            return;
        }

        $path_old_imagen = $this->getAbsolutePathImagen();

        $extension = pathinfo($this->imagenFile->getClientOriginalName(), PATHINFO_EXTENSION);
        $this->imagen = uniqid(sprintf('%s_%s_', $this->capacitacion->getId(), $this->numero)) . '.' . $extension;

        $this->imagenFile->move($this->getUploadRootDirImagen(), $this->imagen);

        $this->imagenFile = null;

        if (is_file($path_old_imagen)) {
            unlink($path_old_imagen);
        }
    }

    public function removeUploadImagen()
    {
        $this->removeImagen();
    }

    public function removeImagen()
    {
        if (($file = $this->getAbsolutePathImagen()) && is_file($file)) {
            unlink($file);
        }
        $this->imagen = null;
    }

    /** @return   \Symfony\Component\HttpFoundation\File\UploadedFile */
    public function getImagenFile()
    {
        return $this->imagenFile;
    }

    /**
     * @param   \Symfony\Component\HttpFoundation\File\UploadedFile
     *
     * @return  Edicion
     */
    public function setImagenFile(\Symfony\Component\HttpFoundation\File\UploadedFile $imagenFile)
    {
        $this->imagenFile = $imagenFile;

        return $this;
    }

    public function getAbsolutePathImagen()
    {
        return null === $this->getImagen() ? null : $this->getUploadRootDirImagen() . '/' . $this->imagen;
    }

    public function getWebPathImagen()
    {
        return null === $this->getImagen() ? null : $this->getUploadDirImagen() . '/' . $this->imagen;
    }

    public function getUploadRootDirImagen()
    {
        return dirname($_SERVER['SCRIPT_FILENAME']) . '/' . $this->getUploadDirImagen();
    }

    public function getUploadDirImagen()
    {
        return 'uploads/campus/capacitacion/imagen';
    }

    // --- Autogenerados ----------------------------------------------------------------------------- //

    /**
     * Get id
     *
     * @return integer
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set presentacion
     *
     * @param string $presentacion
     *
     * @return Edicion
     */
    public function setPresentacion($presentacion)
    {
        $this->presentacion = $presentacion;

        return $this;
    }

    /**
     * Get presentacion
     *
     * @return string
     */
    public function getPresentacion()
    {
        return $this->presentacion;
    }

    /**
     * Set imagen
     *
     * @param string $imagen
     *
     * @return Edicion
     */
    public function setImagen($imagen)
    {
        $this->imagen = $imagen;

        return $this;
    }

    /**
     * Get imagen
     *
     * @return string
     */
    public function getImagen()
    {
        return $this->imagen;
    }

    /**
     * Set descripcion
     *
     * @param string $descripcion
     *
     * @return Edicion
     */
    public function setDescripcion($descripcion)
    {
        $this->descripcion = $descripcion;

        return $this;
    }

    /**
     * Get descripcion
     *
     * @return string
     */
    public function getDescripcion()
    {
        return $this->descripcion;
    }

    /**
     * Set objetivos
     *
     * @param string $objetivos
     *
     * @return Edicion
     */
    public function setObjetivos($objetivos)
    {
        $this->objetivos = $objetivos;

        return $this;
    }

    /**
     * Get objetivos
     *
     * @return string
     */
    public function getObjetivos()
    {
        return $this->objetivos;
    }

    /**
     * Set dirigidoA
     *
     * @param string $dirigidoA
     *
     * @return Edicion
     */
    public function setDirigidoA($dirigidoA)
    {
        $this->dirigidoA = $dirigidoA;

        return $this;
    }

    /**
     * Get dirigidoA
     *
     * @return string
     */
    public function getDirigidoA()
    {
        return $this->dirigidoA;
    }

    /**
     * Set perfilDelEgresado
     *
     * @param string $perfilDelEgresado
     *
     * @return Edicion
     */
    public function setPerfilDelEgresado($perfilDelEgresado)
    {
        $this->perfilDelEgresado = $perfilDelEgresado;

        return $this;
    }

    /**
     * Get perfilDelEgresado
     *
     * @return string
     */
    public function getPerfilDelEgresado()
    {
        return $this->perfilDelEgresado;
    }

    /**
     * Set cupoMinimo
     *
     * @param integer $cupoMinimo
     *
     * @return Edicion
     */
    public function setCupoMinimo($cupoMinimo)
    {
        $this->cupoMinimo = $cupoMinimo;

        return $this;
    }

    /**
     * Get cupoMinimo
     *
     * @return integer
     */
    public function getCupoMinimo()
    {
        return $this->cupoMinimo;
    }

    /**
     * Set cupoMaximo
     *
     * @param integer $cupoMaximo
     *
     * @return Edicion
     */
    public function setCupoMaximo($cupoMaximo)
    {
        $this->cupoMaximo = $cupoMaximo;

        return $this;
    }

    /**
     * Get cupoMaximo
     *
     * @return integer
     */
    public function getCupoMaximo()
    {
        return $this->cupoMaximo;
    }

    /**
     * Set fechaInicio
     *
     * @param \DateTime $fechaInicio
     *
     * @return Edicion
     */
    public function setFechaInicio($fechaInicio)
    {
        $this->fechaInicio = $fechaInicio;

        return $this;
    }

    /**
     * Get fechaInicio
     *
     * @return \DateTime
     */
    public function getFechaInicio()
    {
        return $this->fechaInicio;
    }

    /**
     * Set fechaFin
     *
     * @param \DateTime $fechaFin
     *
     * @return Edicion
     */
    public function setFechaFin($fechaFin)
    {
        $this->fechaFin = $fechaFin;

        return $this;
    }

    /**
     * Get fechaFin
     *
     * @return \DateTime
     */
    public function getFechaFin()
    {
        return $this->fechaFin;
    }

    /**
     * Set fechaFinPublicidad
     *
     * @param \DateTime $fechaFinPublicidad
     *
     * @return Edicion
     */
    public function setFechaFinPublicidad($fechaFinPublicidad)
    {
        $this->fechaFinPublicidad = $fechaFinPublicidad;

        return $this;
    }

    /**
     * Get fechaFinPublicidad
     *
     * @return \DateTime
     */
    public function getFechaFinPublicidad()
    {
        return $this->fechaFinPublicidad;
    }

    /**
     * Set fechaFinInscripcion
     *
     * @param \DateTime $fechaFinInscripcion
     *
     * @return Edicion
     */
    public function setFechaFinInscripcion($fechaFinInscripcion)
    {
        $this->fechaFinInscripcion = $fechaFinInscripcion;

        return $this;
    }

    /**
     * Get fechaFinInscripcion
     *
     * @return \DateTime
     */
    public function getFechaFinInscripcion()
    {
        return $this->fechaFinInscripcion;
    }

    /**
     * Set preciosSugeridos
     *
     * @param string $preciosSugeridos
     *
     * @return Edicion
     */
    public function setPreciosSugeridos($preciosSugeridos)
    {
        $this->preciosSugeridos = $preciosSugeridos;

        return $this;
    }

    /**
     * Get preciosSugeridos
     *
     * @return string
     */
    public function getPreciosSugeridos()
    {
        return $this->preciosSugeridos;
    }

    /**
     * Set metodologia
     *
     * @param string $metodologia
     *
     * @return Edicion
     */
    public function setMetodologia($metodologia)
    {
        $this->metodologia = $metodologia;

        return $this;
    }

    /**
     * Get metodologia
     *
     * @return string
     */
    public function getMetodologia()
    {
        return $this->metodologia;
    }

    /**
     * Set mensajeFinal
     *
     * @param string $mensajeFinal
     *
     * @return Edicion
     */
    public function setMensajeFinal($mensajeFinal)
    {
        $this->mensajeFinal = $mensajeFinal;

        return $this;
    }

    /**
     * Get mensajeFinal
     *
     * @return string
     */
    public function getMensajeFinal()
    {
        return $this->mensajeFinal;
    }

    /**
     * Set created
     *
     * @param \DateTime $created
     *
     * @return Edicion
     */
    public function setCreated($created)
    {
        $this->created = $created;

        return $this;
    }

    /**
     * Get created
     *
     * @return \DateTime
     */
    public function getCreated()
    {
        return $this->created;
    }

    /**
     * Set updated
     *
     * @param \DateTime $updated
     *
     * @return Edicion
     */
    public function setUpdated($updated)
    {
        $this->updated = $updated;

        return $this;
    }

    /**
     * Get updated
     *
     * @return \DateTime
     */
    public function getUpdated()
    {
        return $this->updated;
    }

    /**
     * Set capacitacion
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion $capacitacion
     *
     * @return Edicion
     */
    public function setCapacitacion(\Gse\Campus2Bundle\Entity\Capacitacion $capacitacion = null)
    {
        $this->capacitacion = $capacitacion;

        return $this;
    }

    /**
     * Get capacitacion
     *
     * @return \Gse\Campus2Bundle\Entity\Capacitacion
     */
    public function getCapacitacion()
    {
        return $this->capacitacion;
    }

    /**
     * Add imagenesRecomendadas
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\ImagenRecomendada $imagenesRecomendadas
     *
     * @return Edicion
     */
    public function addImagenesRecomendada(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\ImagenRecomendada $imagenesRecomendadas)
    {
        $this->imagenesRecomendadas[] = $imagenesRecomendadas;
        $imagenesRecomendadas->setEdicion($this);

        return $this;
    }

    /**
     * Remove imagenesRecomendadas
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\ImagenRecomendada $imagenesRecomendadas
     */
    public function removeImagenesRecomendada(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\ImagenRecomendada $imagenesRecomendadas)
    {
        $this->imagenesRecomendadas->removeElement($imagenesRecomendadas);
    }

    /**
     * Get imagenesRecomendadas
     *
     * @return \Doctrine\Common\Collections\ArrayCollection
     */
    public function getImagenesRecomendadas()
    {
        return $this->imagenesRecomendadas;
    }

    /**
     * Add avales
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Aval $avales
     *
     * @return Edicion
     */
    public function addAvale(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Aval $avales)
    {
        $this->avales[] = $avales;
        $avales->setEdicion($this);

        return $this;
    }

    /**
     * Remove avales
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Aval $avales
     */
    public function removeAvale(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Aval $avales)
    {
        $this->avales->removeElement($avales);
    }

    /**
     * Get avales
     *
     * @return \Doctrine\Common\Collections\ArrayCollection
     */
    public function getAvales()
    {
        return $this->avales;
    }

    /**
     * Add estados
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado $estados
     *
     * @return Edicion
     */
    public function addEstado(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado $estados)
    {
        $this->estados[] = $estados;
        $estados->setEdicion($this);

        return $this;
    }

    /**
     * Remove estados
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado $estados
     */
    public function removeEstado(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado $estados)
    {
        $this->estados->removeElement($estados);
    }

    /**
     * Get estados
     *
     * @return \Doctrine\Common\Collections\ArrayCollection
     */
    public function getEstados()
    {
        return $this->estados;
    }

    /**
     * Set estadoActual
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado $estadoActual
     *
     * @return Edicion
     */
    public function setEstadoActual(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado $estadoActual = null)
    {
        $this->estadoActual = $estadoActual;
        $estadoActual->setEdicion($this);

        return $this;
    }

    /**
     * Get estadoActual
     *
     * @return \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Estado
     */
    public function getEstadoActual()
    {
        return $this->estadoActual;
    }

    /**
     * Set createdBy
     *
     * @param \Gse\AppBundle\Entity\Usuario $createdBy
     *
     * @return Edicion
     */
    public function setCreatedBy(\Gse\AppBundle\Entity\Usuario $createdBy = null)
    {
        $this->createdBy = $createdBy;

        return $this;
    }

    /**
     * Get createdBy
     *
     * @return \Gse\AppBundle\Entity\Usuario
     */
    public function getCreatedBy()
    {
        return $this->createdBy;
    }

    /**
     * Set numero
     *
     * @param integer $numero
     *
     * @return Edicion
     */
    public function setNumero($numero)
    {
        $this->numero = $numero;

        return $this;
    }

    /**
     * Get numero
     *
     * @return integer
     */
    public function getNumero()
    {
        return $this->numero;
    }

    /**
     * Add modulos
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Modulo $modulos
     *
     * @return Edicion
     */
    public function addModulo(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Modulo $modulos)
    {
        $this->modulos[] = $modulos;
        $modulos->setEdicion($this);

        return $this;
    }

    /**
     * Remove modulos
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Modulo $modulos
     */
    public function removeModulo(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Modulo $modulos)
    {
        $this->modulos->removeElement($modulos);
    }

    /**
     * Get modulos
     *
     * @return \Doctrine\Common\Collections\ArrayCollection
     */
    public function getModulos()
    {
        return $this->modulos;
    }

    /**
     * Add certificados
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Certificado $certificados
     *
     * @return Edicion
     */
    public function addCertificado(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Certificado $certificados)
    {
        $this->certificados[] = $certificados;
        $certificados->setEdicion($this);

        return $this;
    }

    /**
     * Remove certificados
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Certificado $certificados
     */
    public function removeCertificado(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion\Certificado $certificados)
    {
        $this->certificados->removeElement($certificados);
    }

    /**
     * Get certificados
     *
     * @return \Doctrine\Common\Collections\ArrayCollection
     */
    public function getCertificados()
    {
        return $this->certificados;
    }

    /**
     * Set evaluacionParcialHabilitado
     *
     * @param boolean $evaluacionParcialHabilitado
     *
     * @return Edicion
     */
    public function setEvaluacionParcialHabilitado($evaluacionParcialHabilitado)
    {
        $this->evaluacionParcialHabilitado = $evaluacionParcialHabilitado;

        return $this;
    }

    /**
     * Get evaluacionParcialHabilitado
     *
     * @return boolean
     */
    public function getEvaluacionParcialHabilitado()
    {
        return $this->evaluacionParcialHabilitado;
    }

    /**
     * Set evaluacionParcialBloqueado
     *
     * @param boolean $evaluacionParcialBloqueado
     *
     * @return Edicion
     */
    public function setEvaluacionParcialBloqueado($evaluacionParcialBloqueado)
    {
        $this->evaluacionParcialBloqueado = $evaluacionParcialBloqueado;

        return $this;
    }

    /**
     * Get evaluacionParcialBloqueado
     *
     * @return boolean
     */
    public function getEvaluacionParcialBloqueado()
    {
        return $this->evaluacionParcialBloqueado;
    }

    /**
     * Set evaluacionParcialAprobacionRequerida
     *
     * @param boolean $evaluacionParcialAprobacionRequerida
     *
     * @return Edicion
     */
    public function setEvaluacionParcialAprobacionRequerida($evaluacionParcialAprobacionRequerida)
    {
        $this->evaluacionParcialAprobacionRequerida = $evaluacionParcialAprobacionRequerida;

        return $this;
    }

    /**
     * Get evaluacionParcialAprobacionRequerida
     *
     * @return boolean
     */
    public function getEvaluacionParcialAprobacionRequerida()
    {
        return $this->evaluacionParcialAprobacionRequerida;
    }

    /**
     * Set trabajoPracticoHabilitado
     *
     * @param boolean $trabajoPracticoHabilitado
     *
     * @return Edicion
     */
    public function setTrabajoPracticoHabilitado($trabajoPracticoHabilitado)
    {
        $this->trabajoPracticoHabilitado = $trabajoPracticoHabilitado;

        return $this;
    }

    /**
     * Get trabajoPracticoHabilitado
     *
     * @return boolean
     */
    public function getTrabajoPracticoHabilitado()
    {
        return $this->trabajoPracticoHabilitado;
    }

    /**
     * Set trabajoPracticoBloqueado
     *
     * @param boolean $trabajoPracticoBloqueado
     *
     * @return Edicion
     */
    public function setTrabajoPracticoBloqueado($trabajoPracticoBloqueado)
    {
        $this->trabajoPracticoBloqueado = $trabajoPracticoBloqueado;

        return $this;
    }

    /**
     * Get trabajoPracticoBloqueado
     *
     * @return boolean
     */
    public function getTrabajoPracticoBloqueado()
    {
        return $this->trabajoPracticoBloqueado;
    }

    /**
     * Set trabajoPracticoAprobacionRequerida
     *
     * @param boolean $trabajoPracticoAprobacionRequerida
     *
     * @return Edicion
     */
    public function setTrabajoPracticoAprobacionRequerida($trabajoPracticoAprobacionRequerida)
    {
        $this->trabajoPracticoAprobacionRequerida = $trabajoPracticoAprobacionRequerida;

        return $this;
    }

    /**
     * Get trabajoPracticoAprobacionRequerida
     *
     * @return boolean
     */
    public function getTrabajoPracticoAprobacionRequerida()
    {
        return $this->trabajoPracticoAprobacionRequerida;
    }

    /**
     * Set autoevaluacionHabilitado
     *
     * @param boolean $autoevaluacionHabilitado
     *
     * @return Edicion
     */
    public function setAutoevaluacionHabilitado($autoevaluacionHabilitado)
    {
        $this->autoevaluacionHabilitado = $autoevaluacionHabilitado;

        return $this;
    }

    /**
     * Get autoevaluacionHabilitado
     *
     * @return boolean
     */
    public function getAutoevaluacionHabilitado()
    {
        return $this->autoevaluacionHabilitado;
    }

    /**
     * Set autoevaluacionBloqueado
     *
     * @param boolean $autoevaluacionBloqueado
     *
     * @return Edicion
     */
    public function setAutoevaluacionBloqueado($autoevaluacionBloqueado)
    {
        $this->autoevaluacionBloqueado = $autoevaluacionBloqueado;

        return $this;
    }

    /**
     * Get autoevaluacionBloqueado
     *
     * @return boolean
     */
    public function getAutoevaluacionBloqueado()
    {
        return $this->autoevaluacionBloqueado;
    }

    /**
     * Set evaluacionFinalHabilitado
     *
     * @param boolean $evaluacionFinalHabilitado
     *
     * @return Edicion
     */
    public function setEvaluacionFinalHabilitado($evaluacionFinalHabilitado)
    {
        $this->evaluacionFinalHabilitado = $evaluacionFinalHabilitado;

        return $this;
    }

    /**
     * Get evaluacionFinalHabilitado
     *
     * @return boolean
     */
    public function getEvaluacionFinalHabilitado()
    {
        return $this->evaluacionFinalHabilitado;
    }

    /**
     * Set evaluacionFinalBloqueado
     *
     * @param boolean $evaluacionFinalBloqueado
     *
     * @return Edicion
     */
    public function setEvaluacionFinalBloqueado($evaluacionFinalBloqueado)
    {
        $this->evaluacionFinalBloqueado = $evaluacionFinalBloqueado;

        return $this;
    }

    /**
     * Get evaluacionFinalBloqueado
     *
     * @return boolean
     */
    public function getEvaluacionFinalBloqueado()
    {
        return $this->evaluacionFinalBloqueado;
    }

    /**
     * Set evaluacionFinalAprobacionRequerida
     *
     * @param boolean $evaluacionFinalAprobacionRequerida
     *
     * @return Edicion
     */
    public function setEvaluacionFinalAprobacionRequerida($evaluacionFinalAprobacionRequerida)
    {
        $this->evaluacionFinalAprobacionRequerida = $evaluacionFinalAprobacionRequerida;

        return $this;
    }

    /**
     * Get evaluacionFinalAprobacionRequerida
     *
     * @return boolean
     */
    public function getEvaluacionFinalAprobacionRequerida()
    {
        return $this->evaluacionFinalAprobacionRequerida;
    }

    /**
     * Set trabajoFinalHabilitado
     *
     * @param boolean $trabajoFinalHabilitado
     *
     * @return Edicion
     */
    public function setTrabajoFinalHabilitado($trabajoFinalHabilitado)
    {
        $this->trabajoFinalHabilitado = $trabajoFinalHabilitado;

        return $this;
    }

    /**
     * Get trabajoFinalHabilitado
     *
     * @return boolean
     */
    public function getTrabajoFinalHabilitado()
    {
        return $this->trabajoFinalHabilitado;
    }

    /**
     * Set trabajoFinalBloqueado
     *
     * @param boolean $trabajoFinalBloqueado
     *
     * @return Edicion
     */
    public function setTrabajoFinalBloqueado($trabajoFinalBloqueado)
    {
        $this->trabajoFinalBloqueado = $trabajoFinalBloqueado;

        return $this;
    }

    /**
     * Get trabajoFinalBloqueado
     *
     * @return boolean
     */
    public function getTrabajoFinalBloqueado()
    {
        return $this->trabajoFinalBloqueado;
    }

    /**
     * Set trabajoFinalAprobacionRequerida
     *
     * @param boolean $trabajoFinalAprobacionRequerida
     *
     * @return Edicion
     */
    public function setTrabajoFinalAprobacionRequerida($trabajoFinalAprobacionRequerida)
    {
        $this->trabajoFinalAprobacionRequerida = $trabajoFinalAprobacionRequerida;

        return $this;
    }

    /**
     * Get trabajoFinalAprobacionRequerida
     *
     * @return boolean
     */
    public function getTrabajoFinalAprobacionRequerida()
    {
        return $this->trabajoFinalAprobacionRequerida;
    }

    /**
     * Set edicionMadre
     *
     * @param \Gse\Campus2Bundle\Entity\Capacitacion\Edicion $edicionMadre
     *
     * @return Edicion
     */
    public function setEdicionMadre(\Gse\Campus2Bundle\Entity\Capacitacion\Edicion $edicionMadre = null)
    {
        $this->edicionMadre = $edicionMadre;

        return $this;
    }

    /**
     * Get edicionMadre
     *
     * @return Edicion
     */
    public function getEdicionMadre()
    {
        return $this->edicionMadre;
    }
}