from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_config_v1_eventmonitoring_get import EventConfigV1EventmonitoringGET
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    spec_id: str,
    *,
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_nd_rbac, Unset):
        headers["X-Nd-Rbac"] = x_nd_rbac

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/nexus/infra/api/eventmonitoring/v1/namespaces/{namespace}/eventconfigs/{spec_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventConfigV1EventmonitoringGET]]:
    if response.status_code == 200:
        response_200 = EventConfigV1EventmonitoringGET.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EventConfigV1EventmonitoringGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespace: str,
    spec_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EventConfigV1EventmonitoringGET]]:
    """Get an event configuration

     Get a single event configuration resource being monitored

    Args:
        namespace (str):
        spec_id (str):
        x_nd_rbac (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventConfigV1EventmonitoringGET]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        spec_id=spec_id,
        x_nd_rbac=x_nd_rbac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace: str,
    spec_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EventConfigV1EventmonitoringGET]]:
    """Get an event configuration

     Get a single event configuration resource being monitored

    Args:
        namespace (str):
        spec_id (str):
        x_nd_rbac (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventConfigV1EventmonitoringGET]
    """

    return sync_detailed(
        namespace=namespace,
        spec_id=spec_id,
        client=client,
        x_nd_rbac=x_nd_rbac,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    spec_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EventConfigV1EventmonitoringGET]]:
    """Get an event configuration

     Get a single event configuration resource being monitored

    Args:
        namespace (str):
        spec_id (str):
        x_nd_rbac (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventConfigV1EventmonitoringGET]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        spec_id=spec_id,
        x_nd_rbac=x_nd_rbac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    spec_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EventConfigV1EventmonitoringGET]]:
    """Get an event configuration

     Get a single event configuration resource being monitored

    Args:
        namespace (str):
        spec_id (str):
        x_nd_rbac (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventConfigV1EventmonitoringGET]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            spec_id=spec_id,
            client=client,
            x_nd_rbac=x_nd_rbac,
        )
    ).parsed
